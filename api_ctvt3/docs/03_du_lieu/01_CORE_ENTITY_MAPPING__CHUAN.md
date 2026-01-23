01_CORE_ENTITY_MAPPING__CHUAN.md
(PHẦN 1) – BẢNG hoa_don_ban
________________________________________
1. THÔNG TIN CHUNG
•	Tên bảng DB: hoa_don_ban
•	Entity file: core/entities/hoa_don_ban.py
•	Vai trò:
Header của nghiệp vụ BÁN GAS
→ Đại diện 01 chứng từ bán hàng thực tế
•	Thuộc lớp: CORE_GIAO_DICH (Lớp A)
•	Sinh số khi: trang_thai = 'xac_nhan'
•	Không được dùng để:
o	cập nhật tồn kho
o	cập nhật công nợ
o	cập nhật quỹ
(mọi hệ quả sinh qua JOURNAL)
________________________________________
2. DANH SÁCH CỘT & MAPPING DB → PYTHON
#	Cột DB	Kiểu DB	Bắt buộc	Python type	Ghi chú
1	id	INT	✔	int	PK, auto increment
2	so_hd	VARCHAR(50)	✖	str | None	Số hóa đơn hiển thị
3	ngay	DATE	✖	date | None	Ngày bán
4	ma_kh	VARCHAR(50)	✖	str | None	FK → khach_hang.ma_kh
5	ma_nv	VARCHAR(50)	✖	str | None	FK → nhan_vien.ma_nv
6	ma_kho	VARCHAR(20)	✖	str | None	FK → kho_hang.ma_kho
7	tong_tien	DECIMAL(18,2)	✖	Decimal | None	Tổng tiền hàng
8	tien_mat	DECIMAL(18,2)	✖	Decimal | None	Tiền mặt khách trả
9	tien_ck	DECIMAL(18,2)	✖	Decimal | None	Tiền chuyển khoản
10	tong_thanh_toan	DECIMAL(18,2)	✖	Decimal | None	Tổng tiền đã trả
11	no_lai	DECIMAL(18,2)	✖	Decimal | None	Công nợ còn lại
12	trang_thai	ENUM	✔	TrangThaiChungTu	nhap / xac_nhan / chot / huy
13	ngay_tao	DATETIME	✔	datetime	Tự sinh
📌 Lưu ý kỹ thuật
•	Tất cả trường tiền dùng Decimal, không dùng float
•	ENUM map sang enum Python, không dùng string trần
________________________________________
3. ENUM SỬ DỤNG
trang_thai
•	Nguồn: core/enums/trang_thai_chung_tu.py
•	Giá trị:
o	nhap
o	xac_nhan
o	chot
o	huy
________________________________________
4. QUY TẮC BẤT DI BẤT DỊCH CHO ENTITY NÀY
1.	Entity chỉ mapping DB – không logic
2.	Không có method:
o	tính tiền
o	tính công nợ
o	sinh VAT
3.	Không join bảng khác
4.	Không cập nhật trạng thái ngoài API nghiệp vụ
5.	Mọi điều chỉnh sau xac_nhan → tạo chứng từ mới
________________________________________
5. NHỮNG ĐIỀU BỊ CẤM
•	Thêm field không có trong DB
•	Tính no_lai trong entity
•	Gán mặc định trạng thái bằng code
•	Update trực tiếp số tiền sau khi đã xac_nhan
________________________________________

