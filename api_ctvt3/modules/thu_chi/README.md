# MODULE THU – CHI

Module `thu_chi` xử lý nghiệp vụ thu tiền và chi tiền của công ty.

Phạm vi:
- Ghi nhận phiếu thu
- Ghi nhận phiếu chi

Sau khi ghi nhận:
- Phát sinh sự kiện để ghi sổ quỹ
- Phục vụ kế toán và báo cáo

Nguyên tắc:
- Controller chỉ nhận dữ liệu
- Service xử lý nghiệp vụ
- Core cung cấp luật chung
- Event chỉ mô tả sự kiện đã xảy ra
