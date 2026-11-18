# Team

## Thông tin nhóm

- Tên nhóm: ABC
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NhomABC-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S8

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên                  | MSSV        | Vai                    | Trưởng nhóm |
| --: | -------------------------- | ----------- | ---------------------- | :---------: |
|   1 | Nguyễn Hoàng Văn Tiến Mạnh | 2A202603717 | Vận hành và pháp lý    |     Có      |
|   2 | Lê Hoàng Anh               | 2A202603691 | Kỹ sư cổng             |             |
|   3 | Phan Văn Cường             | 2A202603669 | Sản phẩm và kinh doanh |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## NguyenHoangVanTienManh-2A202603717

### Phần việc phụ trách

Vai trong bàn: Vận hành và pháp lý

Câu nào của đề: 1.2, 1.4, 1.5, 2.4, 2.5, 2.10, 3.0

Mục nào của phiếu A/B/C: A1, A2, A3, A5, B5, B6, B7.5, B8, C0, C1, C12

File nào:

- `templates/form-a-criteria.md`
- `templates/form-b-evaluation-gates.md`
- `config/operating_gates.json`
- `lab10/guards_round1.py`
- `config/operating_gates.round1.json`
- `config/round1.lock`
- `templates/form-c-incident.md`
- `submission/submission.json`
- `.gitattributes`
- `TEAM.md`

### Đóng góp cụ thể

Hoàn thành phần mục tiêu bên liên quan, telemetry production, đọc khoảng tin cậy và kiểm tra bằng chứng ký tiêu chí trong Phiếu A. Phân tích HAZOP, lập checklist chín nhóm việc và pre-mortem; cấu hình cổng vận hành/pháp lý, viết runbook và phương án giờ cao điểm trong Phiếu B.

Chốt cổng vòng 1, đối chiếu report để lập quyết định v1; ghi nhận mốc prepared của S8 và hoàn thiện quyết định v2 Thu hẹp cùng ba dòng bắt buộc. Đồng bộ thông tin bài nộp, gom và kiểm tra đủ thành phần. Khắc phục lỗi integrity do CRLF/LF, bổ sung `.gitattributes` và kiểm tra lại đạt PASS-VISIBLE.

Có sử dụng AI (Codex/ChatGPT) hỗ trợ đọc yêu cầu, lịch sử commit và report; soạn và rà soát nội dung phiếu, cấu hình vận hành/pháp lý, xử lý lỗi định dạng CRLF/LF và kiểm tra hồ sơ nộp. Tôi chịu trách nhiệm kiểm tra kết quả, hiểu và giải thích các ngưỡng, quyết định v1/v2 cùng giới hạn của bằng chứng khi demo.

### Bằng chứng

- Commit: `c7e8880` (1.2), `480ab1d` (1.5), `789b703` (A5), `ebcb92a` (2.4–2.5), `a9a51cf` (chốt cổng vòng 1 và v1), `c5ad5dd` (3.0). Bằng chứng nội dung tại Phiếu A A1–A3/A5, Phiếu B B4–B6/B7.5–B7.6/B8 và Phiếu C C0–C1/C12.
- Kiểm tra cấu hình vận hành: `R-base-after-20261118-171510-d2c575`; chốt vòng 1: hash `02d3f54f`, run `R-base-prepared-20261118-172200-d2c575` — mọi ngưỡng đã ký đạt, chi phí 5.550đ/ticket, ROI 0,80, 0 ca ùn.
- Mốc đầu sự cố: grade `R-S8-grade-20261118-172902-d2c575`, prepared `R-S8-prepared-20261118-172903-d2c575` — còn 1.140.000đ hoàn sai, 5 lỗi hãng oan, kiểm lại 100%; dùng đối chiếu pre-mortem ở C1.
- Kiểm tra hoàn thiện: grade `R-S8-grade-20261118-210524-19ef2e` — PASS-VISIBLE, integrity/criteria/visible/regression/monitor đều đạt, chưa chạy test ẩn. Ba mốc: `R-S8-before-20261118-210524-19ef2e`, `R-S8-prepared-20261118-210524-19ef2e`, `R-S8-after-20261118-210525-19ef2e`; after hoàn sai/lỗi hãng oan/PII đều 0, chi phí 2.978đ/ticket, ROI 2,36. Report được gom trong `submission/runs/`, quyết định v2 Thu hẹp và ba dòng bắt buộc khớp C12 với `submission/submission.json`.
- Lệnh `lab10.check_submission --collect` đã báo ĐỦ THÀNH PHẦN; các cập nhật hoàn thiện C12, hồ sơ nộp và `.gitattributes` hiện chưa có commit mới, không gán vào các commit trước đó.

### Exit ticket

Tôi học được rằng quyết định pilot phải dựa trên tiêu chí đã ký và bằng chứng theo từng phân khúc; cổng kỹ thuật cần đi cùng người duyệt, ngưỡng dừng và quy trình đối soát.

Tôi còn cần xác minh trên pilot thật liệu việc kiểm phê duyệt có chặn được thu hồi đồng thời, và chi phí cùng thời gian chờ có giữ trong ngưỡng khi lượng ticket tăng.

## LeHoangAnh-2A202603691

### Phần việc phụ trách

Vai trong bàn: Kỹ sư cổng.

Câu đã phụ trách: 1.3, 2.1, 2.2, 2.6, 2.7, 2.8, 3.1 (Phiếu C C2, phần S8 ở C3.1/C3.4 và C4).

Mục phiếu: Phiếu A mục A2; Phiếu B mục B0–B2 và B7.1–B7.3; Phiếu C mục C2, C3.1/C3.4 và C4.

File: `lab10/guards.py`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`.

### Đóng góp cụ thể

Thiết kế metric offline đo độ chính xác khi ghi lỗi hãng bằng cách đối chiếu `carrier_id` và `parcel_id` với nhãn chuẩn. Xây các cổng ghim policy hiệu lực, đối chiếu quyền hoàn tiền với tracking/chính sách, xác minh kiện hàng/nguyên nhân trước khi ghi lỗi hãng, chặn hoàn trùng ticket và lọc nội dung/PII khỏi thông báo hãng. Chạy baseline và trace `T-002@55`, ghi nhận 20.000đ hoàn sai và một lỗi hãng oan; sau sửa chạy `after` đạt 110/110, không còn hoàn sai, lỗi hãng oan hay lộ PII. Thử thêm hai ticket adhoc: chặn yêu cầu hoàn trái tracking và giữ được khoản hoàn hợp lệ trong khi loại số điện thoại/ghi chú khỏi thông báo hãng. Với thẻ S8, truy vết và phân biệt ba nguyên nhân dùng approval sai: mã hết hạn, số tiền vượt `max_vnd`, và mã thuộc ticket/đơn khác; ghi tác hại, nguồn lỗi, mức kiểm soát người duyệt và HAZOP vào Phiếu C. Đề xuất hai bước chống overfit theo ticket cụ thể và kiểm tra trên ca độc lập/hidden set.

Có sử dụng AI hỗ trợ đọc cấu trúc repo, rà soát/soạn cổng trong `lab10/guards.py` và diễn giải kết quả vào các phiếu; cần tự nắm và giải thích được các quyết định kỹ thuật khi demo.

### Bằng chứng

Baseline: `R-base-before-20261118-161943-fae142`; sau sửa: `R-base-after-20261118-170020-bc4577` (`runs/R-base-after-20261118-170020-bc4577/report.json`); trace `T-002@55`; hai trace adhoc seed 11 ở Phiếu B B7.3. Thẻ S8: trace `S8-02@11` và `S8-03@11` ở stage base, `S8-04@11` ở prepared; mốc grade `R-S8-grade-20261118-172902-d2c575`. `lab10.gate` xác nhận mọi tiêu chí đã ký đạt trên run after; bộ public có 13 tests, OK. Bằng chứng trong Phiếu A A2, Phiếu B B0–B2/B7.1–B7.3 và Phiếu C C2/C3.1/C3.4/C4.

### Exit ticket

Tôi học được rằng phải kiểm soát lệnh ghi dựa trên nguồn dữ liệu có thẩm quyền, thay vì tin số liệu do model trích từ lời khách khai. Tôi còn cần xác nhận các cổng không làm hỏng ca hợp lệ qua lần chạy `base · after` và `prepared`.

## PhanVanCuong-2A202603669

### Phần việc phụ trách

Vai trong bàn: Sản phẩm và kinh doanh.

Câu nào của đề (theo cột "vai cầm bút" trong `problem-set.md`): 1.1, 1.6, 2.3, 2.9, 3.2, và phần `business` của 3.5.

Mục nào của phiếu A/B/C: Phiếu A mục A1 (câu 1.1) và A4 (câu 1.6 — Bộ tiêu chí và ký); Phiếu B mục B3 (bản đồ dữ liệu, câu 2.3) và B7.4 (cổng `business`, câu 2.9); Phiếu C mục C5 · Câu 3.2 (specification) và C7 · Câu 3.5 (phần `business` của bảng sửa).

File nào: `config/acceptance_criteria.json` (+ `.lock`), `config/operating_gates.json` mục `business`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`.

### Đóng góp cụ thể

**Câu 1.1 (Phiếu A, A1):** viết một mục tiêu cấp hệ thống của trợ lý đã tiền tệ hoá được (không phải "model trả lời đúng"), dựa trên PRD v1.1 §3.

**Câu 1.6 (Phiếu A, A4):** viết toàn bộ **Bộ tiêu chí** và ký: 5 ngưỡng bắt buộc `pass_rate_min=0.95`, `pass_k_min=0.9`, `wrongful_refund_vnd_max=0`, `wrongful_carrier_faults_max=0`, `pii_leaks_max=0`; nhóm `business_ops` (chi phí/ticket ≤ 10.000đ, ROI ≥ 0.2, số ca ùn tối đa); viết `decision_rule`; thêm hai ranh giới đầu ra (một hoãn được, một chuyển người). Chọn ngưỡng an toàn về 0 và lấy trần kinh doanh từ `ops_facts`/`ops_limits` của `data/world.json`.

**Câu 2.3 (Phiếu B, B3):** điền bản đồ dữ liệu (trường then chốt, nguồn sự thật vs bản sao, chỗ thế giới thật làm lệch) và rút ra một ví dụ drift trong 3 tháng tới: cái gì đổi, trường nào lộ, con số tiêu chí nào bị ảnh hưởng, chỉ số nào phát hiện.

**Câu 2.9 (Phiếu B, B7.4):** đặt cổng `business` trong `config/operating_gates.json`: `daily_refund_cap_vnd=2.000.000`, `cost_budget_per_ticket_vnd=1.500`, `pilot_scope={warehouse, [HN, HCM], 100%}`, `roi_min=0.2` — mỗi con số kèm lý do lấy từ `ops_facts`/`ops_limits`.

**Câu 3.2 (Phiếu C, C5):** viết specification mà nếu vi phạm sẽ gây tác hại trên thẻ S8 — "khoản hoàn vượt hạn mức tự động chỉ được ghi khi approval đồng thời đúng phạm vi (ticket/order/customer), còn hiệu lực (status + expires_at ≥ as_of), đủ tiền (amount ≤ max_vnd) và đúng người duyệt"; kiểm bằng code (`_approval_ok`) và bằng con số report (wrongful_refund_vnd phải = 0).

**Câu 3.5 — phần `business` (Phiếu C, C7):** đặt ràng buộc kinh doanh cho bảng sửa (trần tiền/ROI, trả khoản vượt hạn mức về người duyệt), xác nhận biện pháp **ngăn** hay chỉ **giảm**; đọc chi phí/ticket, ROI, trần tiền ở ba mốc và ra quyết định v1 **Thu hẹp** → v2 **Tiếp tục** khi after đạt mọi ngưỡng kinh doanh.

Có sử dụng AI hỗ trợ đọc code/report và rà soát điều kiện tiêu chí; các con số và lý do ngưỡng do tôi tự kiểm và phải tự giải thích được khi demo.

### Bằng chứng

Ký tiêu chí: commit `9f82d7f` (Sign acceptance criteria), hash tiêu chí `992a52e1`; chốt v1: commit `8e92c98` (2.10 v1) trong `templates/form-b-evaluation-gates.md` mục B8 (cả bàn chốt, tôi cầm bút phần kinh doanh/tiêu chí). Mã lần chạy: base `R-S8-before-20261118-202837-19ef2e` (hoàn sai 6.845.000đ, ROI −2,45), prepared `R-S8-prepared-20261118-202837-19ef2e` (11.946đ/ticket, ROI −0,93), after `R-S8-after-20261118-202837-19ef2e` (2.978đ/ticket, ROI 2,36, hoàn sai 0), grade `R-S8-grade-20261118-202837-19ef2e` — "Được phép cân nhắc Tiếp tục". Bằng chứng trong Phiếu A mục A1/A4, Phiếu B mục B3/B7.4, Phiếu C mục C5 · Câu 3.2 và C7 (phần `business`); `config/acceptance_criteria.json` (`required`, `business_ops`, `decision_rule`), `config/operating_gates.json` mục `business`.

### Exit ticket

Tôi học được rằng tiêu chí kinh doanh phải là **ngưỡng tiền/ROI tường minh kèm hành động khi vượt trần**, chứ không chỉ là "chạy đúng"; và ngưỡng an toàn liên quan tiền phải đặt về 0, không thương lượng bằng chi phí. Tôi còn chưa chắc chi phí 2.978đ/ticket và ROI 2,36 ở đây có giữ được trên dữ liệu pilot thật (LLM/ticket thực vẫn dưới trần 1.500đ và khối lượng ticket thật đúng giả định) — cần đo lại trước Bước đánh giá 2.
