# MODULES – NGHIỆP VỤ TRUNG TÂM CỦA API CTVT3

Thư mục `modules/` chứa toàn bộ nghiệp vụ vận hành của công ty CTVT.

Mỗi module tương ứng với MỘT NHÓM NGHIỆP VỤ THỰC TẾ.
Không chia theo kỹ thuật. Không chia cho tiện code.

--------------------------------------------------

## NGUYÊN TẮC BẤT BIẾN

1. CHỈ CÓ 6 MODULE
- ban_gas
- nhap_gas
- thu_chi
- thu_ngan
- ke_toan
- bao_cao

❌ Không tạo module mới nếu không có nghiệp vụ mới thật sự.
❌ Không gom nghiệp vụ cho “đỡ rườm”.

--------------------------------------------------

## VAI TRÒ CHUNG CỦA CÁC THƯ MỤC CON

### controllers/
- Nhận request từ bên ngoài
- Kiểm tra dữ liệu đầu vào
- Gọi service
- KHÔNG chứa nghiệp vụ

### services/
- Điều phối toàn bộ nghiệp vụ
- Gọi core (entity, rules)
- Gọi repository
- Phát sinh event

### commands/
- Biểu diễn “NGƯỜI DÙNG MUỐN LÀM GÌ”
- Không xử lý
- Chỉ là dữ liệu đầu vào cho service

### rules/
- Luật nghiệp vụ RIÊNG của module
- Bổ sung cho luật chung trong core
- Chỉ kiểm tra ĐƯỢC / KHÔNG ĐƯỢC

### events/
- Sự kiện nghiệp vụ ĐÃ XẢY RA
- Là nguồn sinh journal, snapshot, VAT, gas dư
- KHÔNG xử lý trực tiếp

### readers/ (chỉ có ở bao_cao)
- Chỉ đọc dữ liệu
- Không sinh số
- Không ghi DB

--------------------------------------------------

## MỐI QUAN HỆ VỚI CORE

- Core = luật công ty (bất biến)
- Module = thực thi nghiệp vụ theo luật

Module:
- ĐƯỢC dùng core
- KHÔNG được sửa core
- KHÔNG được nhét DB vào core

--------------------------------------------------

## KẾT LUẬN

Nếu còn phân vân:
- Nghiệp vụ ở đâu? → module
- Luật ở đâu? → core
- Ghi sổ ở đâu? → journal / repository
- Báo cáo ở đâu? → bao_cao

File này là luật gốc cho toàn bộ `modules/`.
