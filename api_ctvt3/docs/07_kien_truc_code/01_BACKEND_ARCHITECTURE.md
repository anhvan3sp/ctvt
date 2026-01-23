## Phân định trách nhiệm API và Database

- Controller: nhận request, validate đầu vào.
- Service: xử lý nghiệp vụ, sinh bút toán.
- Repository: chỉ đọc/ghi dữ liệu, không có logic nghiệp vụ.
- Database: lưu trữ dữ liệu, không xử lý nghiệp vụ.
