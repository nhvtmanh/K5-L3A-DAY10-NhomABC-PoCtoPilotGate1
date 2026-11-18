# Tự kiểm tra sự cố S8 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S8-grade-20261118-203129-19ef2e` · bàn: `NhomABC` · grader `lab10-1.0` · 0.938s
- Ba mốc: base `R-S8-before-20261118-203130-19ef2e` · prepared `R-S8-prepared-20261118-203130-19ef2e` · after `R-S8-after-20261118-203130-19ef2e` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `02d3f54f`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `19ef2e412da9`
- Hash Bản tiêu chí chấp nhận: `992a52e15386` · đã ký: `992a52e15386` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S8` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S8 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['data/tickets.jsonl', 'data/world.json', 'incidents/S1/card.json', 'incidents/S1/card.md', 'incidents/S1/tickets.jsonl', 'incidents/S1/world_patch.json', 'incidents/S2/card.json', 'incidents/S2/card.md', 'incidents/S2/tickets.jsonl', 'incidents/S2/world_patch.json', 'incidents/S3/card.json', 'incidents/S3/card.md', 'incidents/S3/tickets.jsonl', 'incidents/S3/world_patch.json', 'incidents/S4/card.json', 'incidents/S4/card.md', 'incidents/S4/tickets.jsonl', 'incidents/S4/world_patch.json', 'incidents/S5/card.json', 'incidents/S5/card.md', 'incidents/S5/tickets.jsonl', 'incidents/S5/world_patch.json', 'incidents/S6/card.json', 'incidents/S6/card.md', 'incidents/S6/tickets.jsonl', 'incidents/S6/world_patch.json', 'incidents/S7/card.json', 'incidents/S7/card.md', 'incidents/S7/tickets.jsonl', 'incidents/S7/world_patch.json', 'incidents/S8/card.json', 'incidents/S8/card.md', 'incidents/S8/tickets.jsonl', 'incidents/S8/world_patch.json', 'lab10/__init__.py', 'lab10/_gradectx.py', 'lab10/_noop_guards.py', 'lab10/agent.py', 'lab10/check_submission.py', 'lab10/checkpoint.py', 'lab10/criteria.py', 'lab10/eval.py', 'lab10/gate.py', 'lab10/grade.py', 'lab10/helpers.py', 'lab10/mock_llm.py', 'lab10/ops.py', 'lab10/tools.py', 'lab10/trace.py', 'lab10/world.py', 'tests/test_public.py'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['approval_gate_block_rate']; sáng đèn: [('approval_gate_block_rate', 'after', 0.0, 0.04)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 1.0 | 1.0 | 0.2 |
| thời gian chờ trung bình (phút) | 107.4 | 9.5 | 0.2 |
| thời gian chờ lâu nhất (phút) | 216.0 | 22.0 | 1.0 |
| số ca bị ùn | 36 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 100 | 100 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 11225 · 10000 | 11946 · 10000 | 2978 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 669 · 1500 | 769 · 1500 | 769 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -1432721 | -276643 | 175557 |
| ROI | -2.45 | -0.93 | 2.36 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 498000 · 2000000 | 24000 · 2000000 | 24000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 1369000 · 2000000 | 228000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.4808 | 0.4808 |
| số kho đắt hơn làm tay | 4 | 2 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 35 | 5 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.8182; hoàn sai 1080000; oan 10; PII 0; chi phí 10652đ > làm tay | — | — |
| kho DN | pass 0.75; hoàn sai 4625000; oan 20; PII 0; chi phí 10650đ > làm tay | — | — |
| kho HCM | pass 0.9231; hoàn sai 1140000; oan 5; PII 0; chi phí 10647đ > làm tay | pass 0.9231; hoàn sai 1140000; oan 5; PII 0; chi phí 10747đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2116đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10645đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10745đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1411đ |
| hãng DNB | pass 0.8182; hoàn sai 2300000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.9091; hoàn sai 520000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 0.8889; hoàn sai 560000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.75; hoàn sai 3465000; oan 15; PII 0 | pass 0.8; hoàn sai 1140000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.3077 | 0.3077 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5550 · 10000 | 5550 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 57853 | 57853 |
| ROI | 1.34 | 0.8 | 0.8 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

Niềm tin của nhân viên duyệt (after, gói nhìn thấy): **đạt**

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2308 | 0.2308 | +0.0035 |
| visible | pass_rate | 0.8654 | 0.96 | 1.0 | +0.1346 |
| visible | pass_k | 0.8654 | 0.96 | 1.0 | +0.1346 |
| visible | wrongful_refund_vnd | 6845000 | 1140000 | 0 | -6845000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 35 | 5 | 0 | -35 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.0 | 0.04 | +0.04 |
