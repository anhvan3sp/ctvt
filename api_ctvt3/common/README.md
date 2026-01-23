# COMMON MODULE

## 1. Mục đích

`common/` là tập hợp các **thành phần dùng chung toàn hệ thống**, mang tính:
- kỹ thuật
- hạ tầng
- tiện ích

⚠️ `common` **KHÔNG chứa nghiệp vụ**
⚠️ `common` **KHÔNG phụ thuộc vào system, master, modules**

---

## 2. Nguyên tắc thiết kế

- Thuần kỹ thuật
- Có thể tái sử dụng ở mọi module
- Không chứa logic kinh doanh
- Không biết dữ liệu thực tế là gì
- Dễ test độc lập

---

## 3. Cấu trúc thư mục

common/
│
├── exceptions/ # Chuẩn hóa lỗi
├── constants/ # Hằng số toàn hệ
├── enums/ # Enum kỹ thuật dùng chung
├── utils/ # Hàm tiện ích
├── validators/ # Validate kỹ thuật
├── decorators/ # Decorator dùng chung
└── pagination/ # Phân trang – sort

yaml
Sao chép mã

---

## 4. Exceptions – Chuẩn hóa lỗi

`exceptions/` định nghĩa **ngôn ngữ lỗi chung** cho toàn hệ thống.

Mục tiêu:
- frontend bắt lỗi thống nhất
- log dễ đọc
- không throw Exception lung tung

---

## 5. Constants – Hằng số toàn hệ

`constants/` chứa:
- cấu hình mặc định
- giá trị kỹ thuật
- tham số dùng lặp lại

⚠️ Không chứa dữ liệu nghiệp vụ.

---

## 6. Enums dùng chung

`enums/` chứa enum:
- trạng thái chung
- tiền tệ
- hình thức thanh toán

⚠️ Enum ở đây **không gắn với module nào cụ thể**

---

## 7. Utils – Hàm tiện ích

`utils/` là các hàm:
- xử lý chuỗi
- xử lý số
- xử lý ngày giờ
- sinh ID

⚠️ Utils:
- không truy DB
- không gọi service
- không xử lý nghiệp vụ

---

## 8. Validators – Validate kỹ thuật

`validators/` dùng để:
- validate request
- validate phân trang
- validate tham số kỹ thuật

⚠️ Không validate logic kinh doanh.

---

## 9. Decorators – Dùng chung

`decorators/` cung cấp:
- kiểm tra quyền
- transaction
- ghi audit

⚠️ Decorator **chỉ điều phối**, không xử lý nghiệp vụ.

---

## 10. Pagination – Phân trang

`pagination/` chuẩn hóa:
- request phân trang
- response phân trang

Giúp API thống nhất format trả về.

---

## 11. Quan hệ phụ thuộc

modules/
system/
master/
↑
common/

markdown
Sao chép mã

- Tất cả được phép dùng `common`
- `common` không phụ thuộc ai

---

## 12. Kết luận

- `common` là **xương sống kỹ thuật**
- Viết đúng từ đầu → đỡ sửa về sau
- Mọi thay đổi trong `common` phải cực kỳ thận trọng
