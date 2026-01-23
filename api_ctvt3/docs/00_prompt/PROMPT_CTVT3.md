# PROMPT_CTVT3 – HIẾN PHÁP DỰ ÁN

- Phiên bản: v1.0
- Ngày chốt: 2026-01-19
- Trạng thái: ĐÃ CHỐT – KHÔNG TỰ Ý SỬA
- Chủ sở hữu quyết định: ADMIN (Sếp)

Prompt Ctvt3
PROMPT DỰ ÁN CTVT3
I. MÔ TẢ DỰ ÁN
CTVT3 là phần mềm quản lý vận hành cho công ty CTVT (kinh doanh gas). Mục tiêu chính là đảm bảo công ty vận hành được hằng ngày, số liệu đúng, không rối, không gian lận, có thể mở rộng về sau mà không phải đập lại hệ thống.
Hệ thống phục vụ hai nhóm chính:
•	Nhân viên: nhập liệu nghiệp vụ thực tế
•	Admin (sếp): quản lý, kiểm soát, đối soát toàn bộ số liệu
________________________________________
II. MỤC TIÊU PHẦN MỀM
•	Tạo phần mềm phục vụ trực tiếp cho công ty CTVT
•	Đáp ứng đầy đủ nhu cầu vận hành thực tế
•	Nhân viên sử dụng app để tạo:
o	Hóa đơn nhập
o	Hóa đơn bán
o	Phiếu thu – chi
o	Phiếu thu ngân
o	Phiếu nhận đặt hàng khách
•	Admin quản lý được:
o	Dữ liệu toàn hệ thống
o	Số dư quỹ công ty
o	Số dư quỹ nhân viên
o	Công nợ khách hàng
o	Công nợ nhà cung cấp
________________________________________
III. PHẠM VI GIAI ĐOẠN 1
•	Chỉ thực hiện BACKEND + API cho dự án CTVT3
•	Thư mục gốc dự án API: apiCTVT3
•	Chưa làm mobile app, UI chi tiết
•	Chat nội bộ chỉ ở mức đơn giản (đã có bảng, chưa tối ưu)
•	Chưa tối ưu hiệu năng nâng cao
________________________________________
IV. NỀN TẢNG THIẾT KẾ (ĐÃ CHỐT – KHÔNG ĐƯỢC PHÁ)
Dự án CTVT3 được xây dựng dựa trên 5 sơ đồ đã chốt:
1.	Sơ đồ 1 – Nghiệp vụ
o	Mô tả các hoạt động thực tế của công ty
o	Trả lời: công ty làm gì, tạo ra gì, ảnh hưởng đến đâu
2.	Sơ đồ 2 – Dữ liệu
o	2A: Giao dịch gốc (hóa đơn, thu chi…)
o	2B: Ghi nhận hệ quả (nhật ký, công nợ, tồn kho…)
o	2C: Tổng hợp / báo cáo
o	2D: Danh mục (master data)
o	2H: Hệ thống (user, quyền, chat)
3.	Sơ đồ 3 – Luồng dữ liệu
o	Dữ liệu đi từ nghiệp vụ → chứng từ → ghi nhận → snapshot
4.	Sơ đồ 4 – Snapshot / Chốt số
o	Chốt quỹ ngày
o	Chốt tồn kho ngày
o	Chốt gas dư ngày
o	Snapshot chỉ là ảnh chụp, có thể xoá & build lại
5.	Sơ đồ 5 – Trạng thái – Phân quyền – Kiểm soát
o	Quyền theo vai trò (admin, kế toán, nhân viên…)
o	Trạng thái chứng từ
o	Khoá dòng tiền và VAT
________________________________________
V. NGUYÊN TẮC BẤT DI BẤT DỊCH
1.	Mọi giao dịch đều bắt nguồn từ nghiệp vụ thực tế
2.	Mọi nghiệp vụ đều phải tạo chứng từ
3.	Chỉ chứng từ hợp lệ mới ảnh hưởng số liệu
4.	Không bảng hay API nào được tự ý sửa số dư
5.	Báo cáo và snapshot không phải nguồn sự thật
6.	Snapshot chỉ để đọc nhanh, không được tính ngược
7.	VAT cân thuế tách khỏi doanh thu
8.	Nhân viên không được tự chốt số
________________________________________
VI. NHỮNG ĐIỀU KHÔNG ĐƯỢC PHÉP (ÁP DỤNG KHI LÀM VIỆC VỚI AI)
•	Mọi thuật ngữ tiếng Anh phải giải thích bằng tiếng Việt
•	Không được đưa tiếng Anh mà không giải nghĩa
•	Không viết dài lan man khi chưa được yêu cầu
•	Không viết code khi chưa đủ tư liệu
•	Không viết code kiểu chắp vá
o	Nếu sửa: phải sửa thành 1 file hoàn chỉnh
•	Không tự ý thay đổi cấu trúc làm hỏng dự án
•	Không tự mở rộng phạm vi khi chưa được sếp cho phép
________________________________________
VII. QUY ƯỚC LÀM API
•	API bám sát DB ctvt3 đã chốt
•	API không chứa logic phá nguyên tắc snapshot
•	API không tính ngược từ báo cáo
•	Mọi endpoint phải rõ:
o	Là nghiệp vụ gì
o	Tạo / đọc / xác nhận cái gì
o	Ảnh hưởng bảng nào
________________________________________
VIII. CÁCH SỬ DỤNG PROMPT NÀY
•	Dán toàn bộ nội dung file này vào đầu mỗi phiên làm việc quan trọng
•	Mọi thiết kế API phải tuân theo nội dung trong file
•	Khi dự án tạm dừng dài ngày, dùng file này để khôi phục tư duy
________________________________________
PROMPT_CTVT3.md – HIẾN PHÁP DỰ ÁN Không được phá, chỉ được mở rộng khi có quyết định rõ ràng từ sếp.
SƠ ĐỒ NGHIỆP VỤ HỆ THỐNG CTVT
(SƠ ĐỒ 1 – BẢN CHUẨN CUỐI – KHÔNG CHỈNH)
________________________________________
I. MỤC ĐÍCH SƠ ĐỒ
Sơ đồ này trả lời 03 câu hỏi duy nhất:
1.	Công ty làm những việc gì
2.	Mỗi việc tạo ra cái gì (chứng từ / ghi nhận)
3.	Việc đó ảnh hưởng đến đâu (kho – tiền – công nợ – VAT – lợi nhuận)
Phạm vi:
•	KHÔNG mô tả bảng CSDL
•	KHÔNG mô tả API
•	CHỈ mô tả nghiệp vụ thực tế
________________________________________
II. DANH SÁCH NGHIỆP VỤ GỐC
Hệ thống CTVT gồm 08 nghiệp vụ chính:
(1) Quản lý danh mục
(2) Nhập gas
(3) Bán gas
(4) Thu – chi phát sinh
(5) Thu ngân (nhân viên nộp tiền)
(6) Đặt hàng (khách / nhà cung cấp)
(7) Quản lý tổng hợp – công nợ – VAT – lợi nhuận
(8) Kế toán dịch vụ – cân thuế VAT
________________________________________
III. CHI TIẾT TỪNG NGHIỆP VỤ
________________________________________
(1) QUẢN LÝ DANH MỤC
Công việc
- Quản lý khách hàng
- Quản lý nhà cung cấp
- Quản lý nhân viên
- Quản lý kho
- Quản lý sản phẩm
- Quản lý danh mục công nợ (chỉ khai báo, không ghi số dư)
Tạo ra
- Thông tin danh mục
Ảnh hưởng
- Không ảnh hưởng kho
- Không ảnh hưởng quỹ
- Không phát sinh công nợ
________________________________________
(2) NHẬP GAS
Công việc
Nhập gas từ nhà cung cấp
Tạo ra
- Hóa đơn nhập
Ảnh hưởng
- Tăng tồn kho gas
- Phát sinh công nợ nhà cung cấp (tiền)
- Phát sinh công nợ vỏ nhà cung cấp (nếu có)
- Giảm quỹ công ty (nếu thanh toán ngay)
- Giảm quỹ nhân viên (nếu nhân viên ứng tiền)
- Nếu thanh toán chuyển khoản:
    + Phát sinh VAT đầu vào
    + VAT được cộng vào giá trị tồn kho
- Giảm kg gas dư (nếu có gas dư trả về NCC)
________________________________________
(3) BÁN GAS ⭐ (NGHIỆP VỤ TRUNG TÂM)
Công việc
Bán gas cho khách hàng
Tạo ra
- Hóa đơn bán
Ảnh hưởng
- Giảm tồn kho gas
- Phát sinh tiền khách trả:
    + Tiền mặt        → quỹ nhân viên
    + Chuyển khoản   → quỹ công ty
- Phát sinh VAT đầu ra (nếu có)
- Phát sinh công nợ khách (nếu bán thiếu)
- Phát sinh công nợ vỏ khách
- Phát sinh gas dư (bán theo kg)
Ghi chú
Một hóa đơn bán có thể đồng thời ảnh hưởng:
kho – tiền – công nợ – vỏ – gas dư – VAT
________________________________________
(4) THU – CHI PHÁT SINH
Công việc
Thu – chi ngoài hóa đơn
(ví dụ: xăng xe, chi phí lặt vặt, ứng trước…)
Tạo ra
- Phiếu thu
- Phiếu chi
Ảnh hưởng
- Quỹ nhân viên (thường là tiền mặt)
- Quỹ công ty
- Công nợ khách / nhà cung cấp (nếu liên quan)
- Có thể phát sinh VAT đầu vào
________________________________________
(5) THU NGÂN (NHÂN VIÊN NỘP TIỀN)
Công việc
Nhân viên bán hàng nộp tiền về công ty
Tạo ra
- Phiếu nộp tiền
Ảnh hưởng
- Giảm quỹ nhân viên
- Tăng quỹ công ty
Ghi chú
- Không tạo doanh thu
- Chỉ là dịch chuyển tiền
________________________________________
(6) ĐẶT HÀNG (KHÁCH / NHÀ CUNG CẤP)
(6.1) Đặt hàng khách (bán trước – thu tiền sau)
Tạo ra
- Phiếu thu
Ảnh hưởng
- Công nợ khách (âm)
- Quỹ nhân viên / quỹ công ty (nếu có thu tiền)
- Có thể phát sinh VAT đầu ra
________________________________________
(6.2) Đặt hàng nhà cung cấp (mua trước – trả tiền sau)
Tạo ra
- Phiếu chi
Ảnh hưởng
- Công nợ nhà cung cấp (dương)
- Quỹ công ty (nếu có chi tiền)
- Có thể phát sinh VAT đầu vào
________________________________________
(7) QUẢN LÝ TỔNG HỢP – CÔNG NỢ – VAT – LỢI NHUẬN
Công việc
- Quản lý hóa đơn VAT (đầu vào / đầu ra)
- Quản lý công nợ khách hàng (tiền + vỏ)
- Quản lý công nợ nhà cung cấp (tiền + vỏ)
- Theo dõi, đối soát số liệu
- Đối soát tồn kho theo kỳ:
    + Tổng nhập
    + Tổng xuất
    + Chênh lệch so với tồn thực tế
- Quản lý lợi nhuận nhân viên theo ngày, tháng
  (chênh lệch giá bán – giá nhận × số lượng bán)
Tạo ra
- Hóa đơn VAT
- Số dư công nợ
- Báo cáo đối soát
- Báo cáo lợi nhuận ngày / tháng
Ảnh hưởng
- Không ảnh hưởng trực tiếp kho
- Không ảnh hưởng trực tiếp quỹ
- Chỉ tổng hợp từ dữ liệu đã phát sinh hợp lệ
________________________________________
(8) KẾ TOÁN DỊCH VỤ – CÂN THUẾ VAT
Bản chất
Xuất hóa đơn VAT không gắn với giao dịch bán thực tế,
chỉ nhằm mục đích cân đối thuế.
Công việc
- Lập hóa đơn VAT không tên / khách lẻ
- Theo dõi VAT cân thuế để phục vụ báo cáo
Tạo ra
- Hóa đơn VAT cân thuế
Ảnh hưởng
- Không ảnh hưởng kho
- Không ảnh hưởng công nợ khách
- Phát sinh VAT đầu ra phải nộp
- Toàn bộ VAT cân thuế được tổng hợp
  và nộp vào tài khoản công ty
Ghi chú
- Không tính vào doanh thu bán hàng
- Không tính vào lợi nhuận nhân viên
________________________________________
IV. TRẠNG THÁI CHỨNG TỪ (ÁP DỤNG TOÀN HỆ THỐNG)
Áp dụng cho:
- Hóa đơn nhập
- Hóa đơn bán
- Phiếu thu
- Phiếu chi
- Phiếu nộp tiền
- Hóa đơn VAT (kể cả VAT cân thuế)
Các trạng thái
(1) Nháp
(2) Đã ghi nhận
(3) Hủy
Nguyên tắc
- Chỉ chứng từ ở trạng thái "Đã ghi nhận"
  mới được dùng để tính:
  kho – quỹ – công nợ – VAT – lợi nhuận
________________________________________
V. NGUYÊN TẮC CHỐT (BẤT DI BẤT DỊCH)
1. Mọi giao dịch đều bắt nguồn từ nghiệp vụ
2. Mọi nghiệp vụ đều tạo ra chứng từ
3. Mỗi chứng từ bắt buộc có trạng thái
4. Chỉ chứng từ hợp lệ mới ảnh hưởng số liệu
5. Không bảng hoặc API nào tự ý thay đổi số dư
6. Báo cáo và chốt số chỉ là tổng hợp dữ liệu hợp lệ
7. Hóa đơn VAT có thể tồn tại độc lập với bán hàng,
   nhưng vẫn phải tổng hợp để báo cáo thuế
________________________________________
SƠ ĐỒ (2): SƠ ĐỒ DỮ LIỆU HỆ THỐNG CTVT3
(Bản chuẩn – thống nhất – không phát sinh thêm sơ đồ)
________________________________________
I. MỤC ĐÍCH SƠ ĐỒ (2)
Sơ đồ (2) được thiết kế để:
1. Chuyển nghiệp vụ (Sơ đồ 1) thành cấu trúc dữ liệu
2. Phân loại rõ vai trò của từng bảng
3. Ngăn việc DB và API làm sai nghiệp vụ
________________________________________
II. CẤU TRÚC TỔNG THỂ CỦA SƠ ĐỒ (2)
Sơ đồ (2) gồm 05 LỚP DỮ LIỆU, KHÔNG PHẢI 05 SƠ ĐỒ RIÊNG.
LỚP A – Dữ liệu giao dịch gốc (Core Transaction)
LỚP B – Dữ liệu ghi nhận hệ quả (Journal / Log)
LỚP C – Dữ liệu tổng hợp – báo cáo (Snapshot)
LỚP D – Dữ liệu danh mục (Master Data)
LỚP H – Dữ liệu hệ thống hỗ trợ (System)
👉 Tất cả nằm trong SƠ ĐỒ (2), chỉ khác vai trò.
________________________________________
III. LỚP A – DỮ LIỆU GIAO DỊCH GỐC
(Nguồn sự thật – không được thiếu)
Định nghĩa
- Mỗi dòng = 1 sự kiện kinh doanh thật
- Sinh ra tiền / kho / công nợ / VAT
- Mất là mất lịch sử
Các bảng
hoa_don_ban
hoa_don_ban_chi_tiet

hoa_don_nhap
hoa_don_nhap_chi_tiet

thu_chi
thu_ngan

hoa_don_vat
gas_du
Nguyên tắc
- Chỉ INSERT
- UPDATE rất hạn chế (trạng thái, ghi chú)
- Tuyệt đối không tính ngược từ bảng khác
________________________________________
IV. LỚP B – DỮ LIỆU GHI NHẬN HỆ QUẢ
(Sinh ra từ lớp A – không được nhập tay)
Định nghĩa
- Ghi lại hậu quả của giao dịch
- Phục vụ truy vết, đối soát, kiểm toán
Các bảng
nhat_ky_kho
nhat_ky_vo
(log thay đổi trạng thái chứng từ – ctvt3 đề xuất)
Nguyên tắc
- Sinh tự động từ lớp A
- Không được dùng làm dữ liệu gốc
- Không được nhập thủ công
________________________________________
V. LỚP C – DỮ LIỆU TỔNG HỢP / BÁO CÁO
(Được xóa – được tạo lại)
Định nghĩa
- Snapshot theo ngày / kỳ
- Chỉ để đọc và báo cáo
Các bảng
ton_kho_chot
ton_kho_chot_ngay

gas_du_chot
gas_du_chot_ngay
Nguyên tắc
- Không được update thủ công
- Không được làm nguồn tính toán
- Có thể xóa và rebuild
________________________________________
VI. LỚP D – DỮ LIỆU DANH MỤC (MASTER DATA)
Định nghĩa
- Đối tượng tham gia nghiệp vụ
- Không tự sinh số liệu
Các bảng
khach_hang
nha_cung_cap
nhan_vien
kho_hang
san_pham
nhan_vien_kho
Nguyên tắc
- Chỉ khai báo
- Không sinh tiền – kho – công nợ
________________________________________
VII. LỚP H – DỮ LIỆU HỆ THỐNG HỖ TRỢ
Định nghĩa
- Phục vụ vận hành phần mềm
- Không tồn tại trong kế toán ngoài đời
Các thành phần
user
phan_quyen / role
dang_nhap / phien_lam_viec
chat_noi_bo
log_truy_cap
log_thao_tac
Nguyên tắc
- Không được chạm dữ liệu lớp A, B, C
- Chỉ kiểm soát quyền truy cập
________________________________________
VIII. QUY TẮC VÀNG CỦA SƠ ĐỒ (2)
1. Mỗi bảng chỉ thuộc MỘT LỚP
2. Bảng lớp A là nguồn duy nhất sinh số
3. Bảng lớp B, C tuyệt đối không tính ngược
4. Danh mục không bao giờ là giao dịch
5. Hệ thống không bao giờ là nghiệp vụ
________________________________________
IX. SƠ ĐỒ TỔNG QUAN (DẠNG CHỮ)
SƠ ĐỒ (1) – NGHIỆP VỤ
        ↓
LỚP A – Giao dịch gốc
        ↓
LỚP B – Ghi nhận hệ quả
        ↓
LỚP C – Tổng hợp / báo cáo

LỚP D – Danh mục (tham gia xuyên suốt)
LỚP H – Hệ thống (bao ngoài, không chạm số)
________________________________________
3. CHỐT CUỐI – SẾP CẦN NHỚ 1 ĐIỀU
Không phải:
“Thêm 2D, 2H”
Mà là:
SƠ ĐỒ (2) có 5 LỚP, mỗi lớp đúng 1 vai
Từ giờ trở đi, sếp chỉ nói:
•	“Bảng này thuộc lớp nào?”
→ là biết đúng hay sai ngay.
________________________________________
👉 BƯỚC TIẾP THEO ĐÚNG TRÌNH TỰ
SƠ ĐỒ (3): KIẾN TRÚC DB CTVT3
•	Danh sách bảng cuối cùng
•	Gộp / tách bảng
•	Loại bỏ bảng sai vai
Khi sếp nói: “Làm Sơ đồ 3”, em làm tiếp.
 
SƠ ĐỒ (3): KIẾN TRÚC DATABASE HỆ THỐNG CTVT3
(Dựa trên Sơ đồ 1 + Sơ đồ 2 – Bản chuẩn triển khai)
________________________________________
I. MỤC ĐÍCH SƠ ĐỒ (3)
Sơ đồ (3) trả lời 4 câu hỏi kỹ thuật cốt lõi:
1. Hệ thống cần những bảng nào (CUỐI CÙNG)
2. Bảng nào là GỐC – bảng nào là PHỤ
3. Bảng nào được INSERT / UPDATE / KHÓA
4. API được phép tác động đến bảng nào
❗ Từ sơ đồ này trở đi:
•	Không thêm bảng tùy hứng
•	Không viết API “cho tiện”
________________________________________
II. PHÂN TẦNG DATABASE (THEO SƠ ĐỒ 2)
CTVT3 DB chia thành 5 nhóm bảng rõ ràng:
A. CORE_GIAO_DICH
B. NHAT_KY_HE_QUA
C. CHOT_BAO_CAO
D. DANH_MUC
H. HE_THONG
________________________________________
III. DANH SÁCH BẢNG CHUẨN THEO TỪNG NHÓM
________________________________________
A. CORE_GIAO_DICH (BẢNG GỐC – NGUỒN SỰ THẬT)
🔒 Nguyên tắc: thiếu 1 bảng là sai nghiệp vụ
hoa_don_ban
hoa_don_ban_chi_tiet

hoa_don_nhap
hoa_don_nhap_chi_tiet

thu_chi
thu_ngan

hoa_don_vat
gas_du
Quy tắc
- INSERT là chính
- UPDATE chỉ cho:
  + trạng thái
  + ghi chú
- Không xóa cứng (chỉ hủy trạng thái)
________________________________________
B. NHAT_KY_HE_QUA (KHÔNG NHẬP TAY)
nhat_ky_kho
nhat_ky_vo
👉 Tương lai CTVT3:
log_chung_tu (đề xuất mới)
Quy tắc
- Chỉ sinh từ CORE_GIAO_DICH
- Không API CRUD trực tiếp
________________________________________
C. CHOT_BAO_CAO (SNAPSHOT – ĐƯỢC XÓA)
ton_kho_chot
ton_kho_chot_ngay

gas_du_chot
gas_du_chot_ngay
Quy tắc
- Không INSERT tay
- Không UPDATE
- Có thể truncate và rebuild
________________________________________
D. DANH_MUC (MASTER DATA)
khach_hang
nha_cung_cap
nhan_vien
kho_hang
san_pham
nhan_vien_kho
Quy tắc
- CRUD có kiểm soát
- Không chứa số dư
________________________________________
H. HE_THONG (KHÔNG LIÊN QUAN NGHIỆP VỤ)
user
user_role
user_permission
user_session

phong_chat
phong_chat_thanh_vien
tin_nhan

audit_log
Quy tắc
- Không JOIN với bảng CORE khi tính số
- Chỉ kiểm soát truy cập
________________________________________
IV. NHỮNG BẢNG CẦN ĐIỀU CHỈNH TỪ CTVT2 → CTVT3
1. GỘP / CHUẨN HÓA
•	hoa_don_ban
➜ thêm cột:
•	trang_thai
•	loai_hoa_don (ban_thuong / ban_kg / can_thue)
•	hoa_don_vat
➜ thêm:
•	loai_phat_sinh (ban_hang / nhap_hang / can_thue)
________________________________________
2. TÁCH LOGIC RA KHỎI BẢNG
❌ Không làm:
cap_nhat_truc_tiep ton kho
cap_nhat cong_no trong khach_hang
✔ Thay bằng:
- tính từ giao dịch
- đối soát bằng nhật ký
________________________________________
3. BẢNG KHÔNG ĐƯỢC PHÉP UPDATE SỐ
nhat_ky_kho
nhat_ky_vo
ton_kho_chot*
gas_du_chot*
________________________________________
V. QUAN HỆ CHUẨN (DẠNG CHỮ – ĐỂ SẾP VẼ INKSCAPE)
[DANH_MUC]
   ↓
[CORE_GIAO_DICH]
   ↓
[NHAT_KY_HE_QUA]
   ↓
[CHOT_BAO_CAO]

[HE_THONG] bao ngoài – không chạm số
________________________________________
VI. NGUYÊN TẮC BẤT DI BẤT DỊCH CỦA SƠ ĐỒ (3)
1. Mọi con số đều xuất phát từ CORE
2. Không bảng nào vừa là gốc vừa là báo cáo
3. Nhật ký chỉ ghi – không tính
4. Chốt chỉ đọc – không sửa
5. User / chat không liên quan kế toán
________________________________________
VII. TÊN FILE CHUẨN ĐỂ LƯU
03_KIENTRUC_DATABASE_CTVT3__CHUAN.txt
________________________________________

SƠ ĐỒ (4): LUỒNG API THEO NGHIỆP VỤ – HỆ THỐNG CTVT3
(Bản chuẩn triển khai – khóa logic hệ thống)
________________________________________
I. MỤC ĐÍCH SƠ ĐỒ (4)
Sơ đồ (4) trả lời 5 câu hỏi sống còn:
1. Mỗi nghiệp vụ gọi API nào
2. API được phép ghi vào bảng nào
3. API sinh ra những hệ quả gì
4. API nào TUYỆT ĐỐI KHÔNG được sửa số
5. Trình tự xử lý để không sai kế toán
❗ Sau sơ đồ này:
•	Không có API “tiện tay update”
•	Không có chuyện “tính lại cho nhanh”
________________________________________
II. NGUYÊN TẮC CHUNG CỦA API CTVT3
1. API chỉ phục vụ NGHIỆP VỤ (theo Sơ đồ 1)
2. API chỉ ghi vào CORE_GIAO_DICH
3. NHAT_KY và CHOT sinh TỰ ĐỘNG
4. API đọc báo cáo KHÔNG ghi DB
5. Không API nào được sửa số dư trực tiếp
________________________________________
III. LUỒNG API THEO TỪNG NGHIỆP VỤ
________________________________________
(1) QUẢN LÝ DANH MỤC
API
POST   /dm/khach-hang
PUT    /dm/khach-hang/{id}

POST   /dm/nha-cung-cap
POST   /dm/nhan-vien
POST   /dm/kho
POST   /dm/san-pham
Ghi DB
khach_hang
nha_cung_cap
nhan_vien
kho_hang
san_pham
nhan_vien_kho
CẤM
- Không ghi kho
- Không ghi tiền
- Không ghi công nợ
________________________________________
(2) NHẬP GAS
API
POST /nhap-gas/hoa-don
POST /nhap-gas/hoa-don/{id}/chi-tiet
POST /nhap-gas/{id}/xac-nhan
Ghi DB (CORE)
hoa_don_nhap
hoa_don_nhap_chi_tiet
hoa_don_vat (nếu có)
Sinh tự động
nhat_ky_kho (nhap)
nhat_ky_vo (nếu có)
Ảnh hưởng
- Tăng tồn kho (tính sau)
- Phát sinh công nợ NCC
- Giảm quỹ (nếu thanh toán)
________________________________________
(3) BÁN GAS ⭐
API
POST /ban-gas/hoa-don
POST /ban-gas/hoa-don/{id}/chi-tiet
POST /ban-gas/{id}/xac-nhan
Ghi DB
hoa_don_ban
hoa_don_ban_chi_tiet
gas_du (nếu bán kg)
hoa_don_vat (nếu có)
Sinh tự động
nhat_ky_kho (xuat)
nhat_ky_vo
Ảnh hưởng
- Giảm tồn kho
- Tăng tiền (NV / công ty)
- Phát sinh công nợ khách
- Phát sinh VAT đầu ra
________________________________________
(4) THU – CHI PHÁT SINH
API
POST /thu-chi/thu
POST /thu-chi/chi
Ghi DB
thu_chi
hoa_don_vat (nếu có)
Ảnh hưởng
- Quỹ nhân viên
- Quỹ công ty
- Có thể liên quan công nợ
________________________________________
(5) THU NGÂN (NV NỘP TIỀN)
API
POST /thu-ngan/nop-tien
Ghi DB
thu_ngan
Ảnh hưởng
- Giảm quỹ NV
- Tăng quỹ công ty
❗ Không sinh doanh thu.
________________________________________
(6) ĐẶT HÀNG
(6.1) Khách đặt trước
API
POST /dat-hang/khach
Ghi DB
thu_chi (thu)
hoa_don_vat (nếu có)
________________________________________
(6.2) Đặt NCC
API
POST /dat-hang/ncc
Ghi DB
thu_chi (chi)
hoa_don_vat (nếu có)
________________________________________
(7) QUẢN LÝ TỔNG HỢP – ĐỐI SOÁT
API
GET /bao-cao/cong-no
GET /bao-cao/ton-kho
GET /bao-cao/loi-nhuan
DB
READ ONLY
❌ CẤM
INSERT / UPDATE / DELETE
________________________________________
(8) KẾ TOÁN DỊCH VỤ – CÂN THUẾ VAT
API
POST /ke-toan/can-thue
Ghi DB
hoa_don_vat (loai = can_thue)
Ảnh hưởng
- Phát sinh VAT phải nộp
- Không ảnh hưởng kho
- Không ảnh hưởng lợi nhuận NV
________________________________________
IV. API HỆ THỐNG (LỚP H)
API
POST /auth/login
POST /auth/logout
GET  /auth/me

POST /chat/phong
POST /chat/tin-nhan
Ghi DB
user
user_session
phong_chat
tin_nhan
audit_log
❗ KHÔNG JOIN – KHÔNG TÍNH SỐ
________________________________________
V. NHỮNG API BỊ CẤM TUYỆT ĐỐI
PUT /ton-kho
PUT /cong-no
PUT /quy
PUT /bao-cao/*
👉 Nếu cần điều chỉnh → tạo chứng từ mới.
________________________________________
VI. LUỒNG TỔNG QUÁT (DẠNG CHỮ – ĐỂ VẼ)
[API nghiệp vụ]
        ↓
[CORE_GIAO_DICH]
        ↓
[Service sinh hệ quả]
        ↓
[NHAT_KY]
        ↓
[JOB chốt kỳ]
        ↓
[BAO_CAO]
________________________________________
VII. NGUYÊN TẮC KHÓA CUỐI CÙNG
1. API không tính – chỉ ghi sự kiện
2. Số liệu luôn tính từ CORE
3. Báo cáo không được ghi
4. Điều chỉnh = chứng từ mới
5. Dev không có quyền sửa số
________________________________________
VIII. TÊN FILE CHUẨN
04_LUONG_API_THEO_NGHIEP_VU_CTVT3__CHUAN.txt

SƠ ĐỒ (5): TRẠNG THÁI – PHÂN QUYỀN – KIỂM SOÁT QUỸ
CTVT3 – BẢN CHUẨN CUỐI (PHÙ HỢP CÔNG TY NHỎ – SẴN SÀNG NÂNG CẤP)
________________________________________
I. MỤC ĐÍCH SƠ ĐỒ (5)
Sơ đồ (5) dùng để:
1.	Xác định AI được làm CÁI GÌ
2.	Xác định CHỨNG TỪ đi qua các TRẠNG THÁI nào
3.	Khóa dòng tiền: tiền mặt – chuyển khoản – VAT
4.	Cho phép vận hành linh hoạt hiện tại
5.	Nhưng KHÔNG phá được số liệu về sau
👉 Sơ đồ (5) không tạo nghiệp vụ mới
👉 Chỉ kiểm soát con người + quyền + trạng thái
________________________________________
II. DANH SÁCH VAI TRÒ (ROLE) CHUẨN
CTVT3 có 5 vai trò, phù hợp quy mô hiện tại:
1.	ADMIN (Sếp)
2.	KẾ TOÁN
3.	NHÂN VIÊN ĐẶC BIỆT
4.	NHÂN VIÊN
5.	KẾ TOÁN ONLINE
________________________________________
III. QUYỀN CHI TIẾT THEO TỪNG VAI TRÒ
________________________________________
(1) ADMIN (SẾP)
Nguyên tắc
•	Không hạn chế
•	Toàn quyền
•	Có thể làm thay mọi vai trò
Quyền
•	CRUD toàn bộ danh mục
•	Lập / sửa / hủy mọi chứng từ
•	Chuyển mọi trạng thái chứng từ
•	Xem, chốt, mở lại mọi báo cáo
•	Quản lý cấu hình hệ thống
👉 ADMIN = quyền cứu hộ + quyền kiểm soát cuối
________________________________________
(2) KẾ TOÁN (KẾ TOÁN NỘI BỘ)
Vai trò cốt lõi
•	Chủ chứng từ
•	Chủ dòng tiền
•	Chủ báo cáo
ĐƯỢC PHÉP
•	Lập & xác nhận:
o	Hóa đơn bán
o	Hóa đơn nhập
o	Phiếu thu
o	Phiếu chi
o	Phiếu thu ngân
•	Xác nhận chuyển khoản
•	Quản lý quỹ công ty:
o	Tiền mặt (két)
o	Tiền ngân hàng (CK)
•	Xem / lập / chốt báo cáo:
o	Công nợ
o	Tồn kho
o	Lợi nhuận
o	VAT
KHÔNG ĐƯỢC
•	Sửa số liệu đã chốt kỳ
•	Can thiệp trực tiếp vào bảng tổng hợp
________________________________________
(3) NHÂN VIÊN ĐẶC BIỆT
(Giai đoạn chuyển tiếp – đúng thực tế hiện tại)
Bản chất
•	Nhân viên kiêm nhiệm
•	Quyền rộng hơn nhân viên thường
•	Phục vụ vận hành khi chưa có kế toán riêng
ĐƯỢC PHÉP
•	Bán hàng
•	Nhập hàng
•	Lập chứng từ ở trạng thái NHÁP:
o	Hóa đơn bán
o	Hóa đơn nhập
o	Phiếu thu
o	Phiếu chi
•	Thu tiền mặt
•	Lập báo cáo ngày:
o	Nhập – xuất – thu – chi
o	Quỹ nhân viên cuối ngày
KHÔNG ĐƯỢC
•	Chốt hóa đơn
•	Xác nhận chuyển khoản
•	Chốt báo cáo
•	Sửa số liệu đã xác nhận
👉 Đây là vai trò “đệm”, khi có kế toán chuẩn → giảm quyền hoặc bỏ.
________________________________________
(4) NHÂN VIÊN (MÔ HÌNH CHUẨN SAU NÀY)
Vai trò
•	Thực hiện nghiệp vụ
•	Không giữ quyền quyết định tài chính
ĐƯỢC PHÉP
•	Bán hàng
•	Nhập hàng
•	Thu – chi lặt vặt
•	Lập báo cáo ngày của chính mình
KHÔNG ĐƯỢC
•	Lập hóa đơn chính thức
•	Chốt chứng từ
•	Xem báo cáo tài chính
•	Ghi nhận VAT
________________________________________
(5) KẾ TOÁN ONLINE
Bản chất
•	Không tham gia vận hành nội bộ
•	Chỉ phục vụ báo cáo thuế
ĐƯỢC PHÉP
•	Nhập hóa đơn VAT cân thuế
•	Xem tổng VAT đầu ra (read-only)
KHÔNG ĐƯỢC
•	Chạm hóa đơn bán / nhập
•	Chạm quỹ
•	Chạm công nợ
•	Chạm lợi nhuận
👉 VAT cân thuế:
•	Không gắn bán hàng
•	Không tính doanh thu
•	Không tính lợi nhuận
________________________________________
IV. TRẠNG THÁI CHỨNG TỪ (ÁP DỤNG CHUNG)
1. Hóa đơn bán / nhập
NHÁP
  ↓
ĐÃ XÁC NHẬN
  ↓
ĐÃ CHỐT
  ↓
(ĐIỀU CHỈNH BẰNG CHỨNG TỪ MỚI)
Quyền chuyển
•	NV / NV đặc biệt: NHÁP → ĐÃ XÁC NHẬN
•	Kế toán / Admin: ĐÃ XÁC NHẬN → ĐÃ CHỐT
________________________________________
2. Phiếu thu – chi
NHÁP → ĐÃ XÁC NHẬN
________________________________________
3. Hóa đơn VAT
TẠO → ĐÃ GHI NHẬN THUẾ
________________________________________
V. QUY TẮC VAT & CHUYỂN KHOẢN
QUY TẮC TỰ ĐỘNG
•	Mọi hóa đơn:
o	Nhập chuyển khoản
o	Bán hàng chuyển khoản
→ TỰ ĐỘNG SINH VAT
Phân loại VAT
•	VAT đầu vào → từ nhập hàng
•	VAT đầu ra → từ bán hàng
•	VAT cân thuế → kế toán online nhập
________________________________________
VI. QUỸ CÔNG TY – CHỐT Ở MỨC VẬN HÀNH
QUỸ CÔNG TY
├── TIỀN MẶT (KÉT)
└── TIỀN NGÂN HÀNG (CK)
Quyền
•	Nhân viên / NV đặc biệt: KHÔNG chạm
•	Kế toán: quản lý
•	Admin: toàn quyền
________________________________________
VII. NGUYÊN TẮC KHÓA CUỐI (BẤT DI BẤT DỊCH)
1.	Quyền gắn với VAI TRÒ, không gắn người
2.	Nhân viên không tự chốt số
3.	Chuyển khoản luôn qua kế toán
4.	VAT sinh tự động theo dòng tiền CK
5.	VAT cân thuế tách khỏi doanh thu
6.	Chuẩn hoá từ từ, không bóp vận hành hiện tại
________________________________________
VIII. TÊN FILE CHUẨN (LƯU DÙNG LÂU DÀI)
05_TRANG_THAI__PHAN_QUYEN__KIEM_SOAT_QUY_CTVT3__CHUAN.txt
________________________________________

---
## QUY ƯỚC QUẢN TRỊ TÀI LIỆU

- File này là HIẾN PHÁP của dự án CTVT3.
- Mọi thiết kế DB, API, CODE đều phải tuân theo.
- Chỉ ADMIN (Sếp) mới có quyền quyết định thay đổi.
- Mọi thay đổi phải ghi rõ:
  - Ngày thay đổi
  - Lý do
  - Phạm vi ảnh hưởng
- Cấm sửa âm thầm.
---
