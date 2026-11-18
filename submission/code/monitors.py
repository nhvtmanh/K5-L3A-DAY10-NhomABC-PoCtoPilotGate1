"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def approval_gate_block_rate(trials):
    """Tỉ lệ lần chạy mà cổng phê duyệt (vòng 2) đã chặn một khoản vượt hạn mức
    vì approval sai phạm vi / hết hạn / thu hồi / vượt max / sai người duyệt.

    Sự kiện do guards.py ghi khi _approval_ok trả False: {"type": "guard",
    "gate": "approval_gate_block", ...}. Đây là tín hiệu "cổng đang làm việc" và
    cũng là proxy cho mức độ dữ liệu phê duyệt bẩn trong luồng, không cần nhãn đúng/sai.
    """
    blocked = sum(any(e.get("gate") == "approval_gate_block" for e in t.get("events", []))
                  for t in trials)
    return blocked / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "approval_gate_block_rate": approval_gate_block_rate,   # metric mới vòng 2 (thẻ S8)
}
STARTER_MONITORS = ("escalation_rate",)
