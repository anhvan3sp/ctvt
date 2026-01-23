# MODULE NHẬP GAS

Module `nhap_gas` xử lý toàn bộ nghiệp vụ nhập gas từ nhà cung cấp.

Phạm vi:
- Tạo hóa đơn nhập
- Thêm chi tiết nhập
- Xác nhận (chốt) hóa đơn nhập

Sau khi xác nhận hóa đơn nhập, hệ thống phát sinh sự kiện để:
- ghi nhận tồn kho
- ghi nhận công nợ nhà cung cấp
- phục vụ kế toán và báo cáo

Nguyên tắc:
- Controller chỉ nhận dữ liệu
- Service điều phối nghiệp vụ
- Core cung cấp luật và entity
- Event chỉ mô tả sự kiện đã xảy ra
