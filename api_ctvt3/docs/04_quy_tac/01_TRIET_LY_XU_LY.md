# TRIẾT LÝ XỬ LÝ HỆ THỐNG CTVT3

## 1. Nguyên tắc cốt lõi
- API (Backend) chịu trách nhiệm xử lý toàn bộ nghiệp vụ.
- Database (DB) chỉ có nhiệm vụ lưu trữ dữ liệu và đảm bảo tính toàn vẹn.

## 2. Database KHÔNG ĐƯỢC LÀM
- Không xử lý nghiệp vụ.
- Không cộng trừ tiền bằng trigger.
- Không tự sinh công nợ, số dư, quỹ.
- Không chứa logic điều kiện kinh doanh.

## 3. Database ĐƯỢC PHÉP LÀM
- Lưu dữ liệu gốc.
- Ràng buộc khóa ngoại.
- Ràng buộc NOT NULL, UNIQUE.
- CHECK đơn giản (>= 0, enum).
- VIEW phục vụ đọc báo cáo (read-only).

## 4. API PHẢI LÀM
- Tạo, sửa, huỷ chứng từ.
- Kiểm tra điều kiện nghiệp vụ.
- Sinh bút toán (ledger).
- Cập nhật quỹ, công nợ thông qua bút toán.
- Đảm bảo rollback khi lỗi.

## 5. Nguyên tắc tiền tệ
- Mọi biến động tiền đều phải đi qua bảng but_toan.
- Không cập nhật trực tiếp số dư.
- Số dư luôn được tính từ tổng but_toan.
