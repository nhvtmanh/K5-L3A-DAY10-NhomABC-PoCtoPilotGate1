"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Pin the policy that is effective today. Without this, an active-index
    # change between runs can silently change the refund rule mid-pilot.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách có hiệu lực; cần người kiểm tra")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("không xác minh được chủ đơn từ dữ liệu nguồn")

        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of)
        if policy is None:
            return Verdict.escalate("không xác định được chính sách có hiệu lực")

        # Refund entitlement comes from tracking and policy, never from the
        # delay claimed in customer text or a model proposal.
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
        entitled = H.entitlement_vnd(policy, order, delay, cause)
        if entitled <= 0:
            return Verdict.deny("đối chiếu tracking và chính sách: đơn chưa đủ điều kiện hoàn")

        # Make the write idempotent across retries and prevent a duplicate
        # ledger entry for a ticket that has already been processed.
        prior = ctx.tools.ledger_rows(ticket_id=action.get("ticket_id"))
        if prior:
            return Verdict.deny("ticket này đã có khoản hoàn trong sổ cái")

        if action.get("amount_vnd", 0) != entitled or action.get("payer") != "LOGIX":
            return Verdict.modify("chuẩn hóa số tiền theo entitlement từ DB và chính sách",
                                  amount_vnd=entitled, payer="LOGIX", basis="policy")

    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("không xác minh được đơn trước khi ghi lỗi cho hãng")
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of)
        if policy is None:
            return Verdict.escalate("không xác định được chính sách có hiệu lực")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        # A carrier fault affects a third party. Require a recorded cause and
        # a policy-eligible delay, then bind the write to that parcel/carrier.
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không chứng minh lỗi thuộc hãng theo chính sách")
        expected = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                    "driver_id": parcel.get("driver_id"), "delay_days": delay}
        if any(action.get(key) != value for key, value in expected.items()):
            return Verdict.modify("đối chiếu lại kiện hàng, hãng và độ trễ từ tracking", **expected)

    elif tool == "notify_carrier":
        # Ticket text and recipient contact details are not needed by the
        # carrier to investigate the delivery exception.
        payload = action.get("payload") or {}
        safe_payload = {k: v for k, v in payload.items()
                        if k not in {"customer_note", "recipient_contact", "phone", "name", "street"}}
        if safe_payload != payload:
            return Verdict.modify("loại bỏ nội dung ticket và thông tin liên hệ khỏi thông báo hãng",
                                  payload=safe_payload)

    return Verdict.allow()
