# MODULE BÁN GAS

Module `ban_gas` xử lý toàn bộ nghiệp vụ bán gas cho khách hàng.

Phạm vi:
- Tạo hóa đơn bán
- Thêm chi tiết bán
- Xác nhận hóa đơn bán
- Phát sinh sự kiện để:
  - ghi nhật ký kho
  - ghi công nợ
  - ghi sổ quỹ

Module này:
- SỬ DỤNG core (entity, rules, value_objects)
- KHÔNG sửa core
- KHÔNG ghi database trực tiếp ở controller

Luồng chuẩn:
Command → Service → Core Rules → Repository → Event
