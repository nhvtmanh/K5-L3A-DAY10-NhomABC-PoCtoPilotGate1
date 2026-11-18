# Team

## Thông tin nhóm

- Tên nhóm: ABC
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NhomABC-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên                  | MSSV        | Vai                    | Trưởng nhóm |
| --: | -------------------------- | ----------- | ---------------------- | :---------: |
|   1 | Nguyễn Hoàng Văn Tiến Mạnh | 2A202603717 | Vận hành và pháp lý    |             |
|   2 | Lê Hoàng Anh               | 2A202603691 | Kỹ sư cổng             |             |
|   3 | Phan Văn Cường             | 2A202603669 | Sản phẩm và kinh doanh |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## NguyenHoangVanTienManh-2A202603717

### Phần việc phụ trách

Vai trong bàn: Vận hành và pháp lý

Câu nào của đề: 1.2, 1.4, 1.5, 2.4, 2.5

Mục nào của phiếu A/B/C: A1, A2, A3, A5, B5, B6

File nào: `templates/form-a-criteria.md`

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit,
mã lần chạy (`runs/<mã>`),
dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LeHoangAnh-2A202603691

### Phần việc phụ trách

Vai trong bàn: Kỹ sư cổng.

Câu đã phụ trách: 1.3, 2.1, 2.2; xây cổng kỹ thuật cho câu 2.6.

Mục phiếu: Phiếu A mục A2; Phiếu B mục B0–B2 và B7.1.

File: `lab10/guards.py`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`.

### Đóng góp cụ thể

Thiết kế metric offline đo độ chính xác khi ghi lỗi hãng bằng cách đối chiếu `carrier_id` và `parcel_id` với nhãn chuẩn. Xây các cổng đối chiếu quyền hoàn tiền với tracking/chính sách, xác minh lỗi hãng trước khi ghi, và loại nội dung ticket/thông tin liên hệ khỏi thông báo cho hãng. Chạy baseline và trace `T-002@55`; ghi nhận hoàn sai 20.000đ, một lỗi hãng oan, phân tích nguyên nhân và đề xuất xử lý trong Phiếu B.

Có sử dụng AI hỗ trợ đọc cấu trúc repo, rà soát/soạn cổng trong `lab10/guards.py` và diễn giải kết quả vào các phiếu; cần tự nắm và giải thích được các quyết định kỹ thuật khi demo.

### Bằng chứng

Baseline: `R-base-before-20261118-161943-fae142` (`runs/R-base-before-20261118-161943-fae142/report.json`); trace `T-002@55`. Bộ kiểm tra công khai: `python -m unittest discover -s tests` — 13 tests, OK. Nội dung đã ghi tại Phiếu A A2 và Phiếu B B0–B2, B7.1.

### Exit ticket

Tôi học được rằng phải kiểm soát lệnh ghi dựa trên nguồn dữ liệu có thẩm quyền, thay vì tin số liệu do model trích từ lời khách khai. Tôi còn cần xác nhận các cổng không làm hỏng ca hợp lệ qua lần chạy `base · after` và `prepared`.

## PhanVanCuong-2A202603669

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
