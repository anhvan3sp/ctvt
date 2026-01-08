# Database – CTVT

## 1. Vai trò của Database
Database (DB) là **nền móng cốt lõi** của toàn bộ hệ thống CTVT.

Mọi thành phần khác đều **phụ thuộc vào DB**:
- Backend API lấy dữ liệu từ DB
- Ứng dụng Android hiển thị và thao tác qua API
- Báo cáo, thống kê, công nợ, tồn kho đều dựa vào DB

👉 Nếu DB sai hoặc rối → toàn hệ thống sai theo.

---

## 2. Hiện trạng Database
Database hiện tại đã được xây dựng để phục vụ hoạt động thực tế của Công ty Văn, bao gồm:
- Bán gas (bán buôn, bán lẻ)
- Quản lý tồn kho gas và vỏ bình
- Theo dõi công nợ khách hàng và nhà cung cấp
- Ghi nhận thu – chi, dòng tiền
- Một số báo cáo tổng hợp bằng VIEW
- Một số xử lý tự động bằng TRIGGER

Tuy nhiên:
- Schema có **nhiều bảng**
- Có **nhiều trigger và view**
- Logic nghiệp vụ đang bị **đẩy nhiều xuống DB**
- Chưa có tài liệu tổng hợp và sơ đồ rõ ràng

👉 Vì vậy, **DB hiện tại khó nắm bắt và khó mở rộng nếu không chuẩn hoá lại**.

---

## 3. Mục tiêu với Database
Mục tiêu của DB trong dự án CTVT là:
- Phản ánh đúng nghiệp vụ thực tế của công ty
- Dữ liệu rõ ràng, nhất quán
- Dễ kiểm soát, dễ sửa, dễ mở rộng
- Làm nền tảng vững chắc cho API và Android

DB **không chạy theo phức tạp kỹ thuật**, ưu tiên:
- Rõ ràng
- Dễ hiểu
- Dễ bảo trì

---

## 4. Cấu trúc thư mục DB
Thư mục `db/` được tổ chức như sau:

# Database – CTVT

## 1. Vai trò của Database
Database (DB) là **nền móng cốt lõi** của toàn bộ hệ thống CTVT.

Mọi thành phần khác đều **phụ thuộc vào DB**:
- Backend API lấy dữ liệu từ DB
- Ứng dụng Android hiển thị và thao tác qua API
- Báo cáo, thống kê, công nợ, tồn kho đều dựa vào DB

👉 Nếu DB sai hoặc rối → toàn hệ thống sai theo.

---

## 2. Hiện trạng Database
Database hiện tại đã được xây dựng để phục vụ hoạt động thực tế của Công ty Văn, bao gồm:
- Bán gas (bán buôn, bán lẻ)
- Quản lý tồn kho gas và vỏ bình
- Theo dõi công nợ khách hàng và nhà cung cấp
- Ghi nhận thu – chi, dòng tiền
- Một số báo cáo tổng hợp bằng VIEW
- Một số xử lý tự động bằng TRIGGER

Tuy nhiên:
- Schema có **nhiều bảng**
- Có **nhiều trigger và view**
- Logic nghiệp vụ đang bị **đẩy nhiều xuống DB**
- Chưa có tài liệu tổng hợp và sơ đồ rõ ràng

👉 Vì vậy, **DB hiện tại khó nắm bắt và khó mở rộng nếu không chuẩn hoá lại**.

---

## 3. Mục tiêu với Database
Mục tiêu của DB trong dự án CTVT là:
- Phản ánh đúng nghiệp vụ thực tế của công ty
- Dữ liệu rõ ràng, nhất quán
- Dễ kiểm soát, dễ sửa, dễ mở rộng
- Làm nền tảng vững chắc cho API và Android

DB **không chạy theo phức tạp kỹ thuật**, ưu tiên:
- Rõ ràng
- Dễ hiểu
- Dễ bảo trì

---

## 4. Cấu trúc thư mục DB
Thư mục `db/` được tổ chức như sau:

db/
├─ schema/ : cấu trúc CSDL (table, khóa, quan hệ)
├─ seed/ : dữ liệu mẫu (nếu cần)
├─ backup/ : file sao lưu, dump từ hệ thống đang chạy

---

## 5. Quy ước quản lý schema
- Schema CSDL được quản lý bằng các file `.sql`
- Mỗi file thể hiện **một giai đoạn hoặc một thay đổi**
- Không chỉnh sửa file schema cũ sau khi đã chốt
- Mọi thay đổi mới phải tạo file mới

Ví dụ:
- `001_init.sql` : khởi tạo cấu trúc CSDL ban đầu
- `002_*.sql`    : các thay đổi tiếp theo

---

## 6. Nguyên tắc thiết kế (đang được rà soát)
Một số nguyên tắc đang được xác định lại để chuẩn hoá DB:
- Phân biệt rõ:
  - **Khoá kỹ thuật (id)**  
  - **Mã nghiệp vụ (ma_kh, ma_nv, …)**
- Hạn chế đưa logic nghiệp vụ phức tạp xuống DB
- Trigger và View chỉ dùng khi thật sự cần thiết
- Ưu tiên để API xử lý nghiệp vụ

> Các nguyên tắc này đang trong quá trình rà soát và điều chỉnh.

---

## 7. Trạng thái hiện tại
- DB đang được **đánh giá và chuẩn hoá lại**
- Chưa triển khai API chính thức
- Chưa khoá thiết kế cuối cùng

👉 **Chưa được phép xây dựng API dựa trên DB này khi chưa chốt schema chuẩn.**

---

## 8. Ghi chú quan trọng
- DB hiện tại là **tài sản nghiệp vụ quan trọng**
- Mọi thay đổi cần được cân nhắc kỹ
- Ưu tiên hiểu rõ trước khi chỉnh sửa
- Không chạy nhanh khi nền móng chưa chắc
