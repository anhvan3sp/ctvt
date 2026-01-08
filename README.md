# CTVT – Phần mềm bán hàng Công ty Văn

## 1. Giới thiệu
CTVT là dự án phần mềm quản lý bán hàng cho **Công ty Văn** – doanh nghiệp kinh doanh **gas bán buôn và bán lẻ**.

Phần mềm nhằm tin học hoá toàn bộ hoạt động:
- Bán hàng
- Quản lý tồn kho
- Quản lý công nợ
- Theo dõi dòng tiền
- Hỗ trợ vận hành hằng ngày tại cửa hàng

---

## 2. Mục tiêu dự án
- Xây dựng **hệ thống bán hàng đơn giản, dễ dùng**, phù hợp thực tế cửa hàng gas
- Quản lý chính xác:
  - Hóa đơn bán / nhập
  - Tồn kho gas, vỏ bình
  - Công nợ khách hàng và nhà cung cấp
- Hạn chế sai sót do ghi chép thủ công
- Có thể mở rộng trong tương lai (báo cáo, VAT, chat nội bộ…)

---

## 3. Phạm vi hệ thống
Dự án gồm các thành phần chính:

- **Database (MySQL)**  
  Lưu trữ dữ liệu nghiệp vụ: khách hàng, hàng hoá, hóa đơn, công nợ, tồn kho…

- **Backend API**  
  Xử lý logic nghiệp vụ, cung cấp dữ liệu cho ứng dụng

- **Ứng dụng Android**  
  Giao diện cho nhân viên bán hàng, kế toán, quản lý

---

## 4. Đối tượng sử dụng
- Chủ doanh nghiệp
- Nhân viên bán hàng
- Kế toán


---

## 5. Trạng thái hiện tại
- Dự án đang ở **giai đoạn chuẩn hoá thiết kế**
- Đang rà soát và xây dựng lại **schema CSDL cho đúng và dễ quản lý**
- **Chưa triển khai API chính thức**
- **Chưa kết nối Android với dữ liệu thật**

> Ưu tiên làm đúng nền móng trước khi phát triển chức năng.

---

## 6. Quy ước chung
- Database là nền tảng gốc của toàn hệ thống
- Schema CSDL được quản lý bằng các file `.sql`
- Không làm API khi schema chưa ổn định
- Mỗi thay đổi lớn đều phải có ghi chú rõ ràng

---

## 7. Ghi chú
- Dự án được xây dựng theo nhu cầu thực tế của Công ty Văn
- Ưu tiên **đơn giản – rõ ràng – dễ bảo trì**
- Không chạy theo kỹ thuật phức tạp khi chưa cần thiết
