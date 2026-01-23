# QUY TRÌNH TRIỂN KHAI & TEST API CTVT3
(BẢN CHUẨN – KHÓA SAI SỐ – TEST THEO SỰ KIỆN)

---

## I. MỤC ĐÍCH

Tài liệu này quy định **CÁCH TEST & TRIỂN KHAI** API CTVT3 để:
1. Đảm bảo **không sinh số sai**
2. Test đúng **sự kiện nghiệp vụ**
3. Phát hiện sai lệch **trước khi chạy thật**

👉 Test = kiểm soát rủi ro kế toán, không phải chỉ check API chạy.

---

## II. NGUYÊN TẮC TEST BẮT BUỘC

1. Test theo **SỰ KIỆN**, không theo endpoint
2. Test **trạng thái chứng từ**
3. Test **ảnh hưởng nghiệp vụ**
4. Test **KHÔNG sinh số ngoài CORE**
5. Test **READ ONLY** cho báo cáo

❌ Không test “cho có”.

---

## III. MÔI TRƯỜNG TEST

### 1. Database
- DB riêng: `ctvt3_test`
- Không dùng DB thật

### 2. Dữ liệu test
- Danh mục test riêng:
  - 1 kho
  - 2 sản phẩm
  - 1 NV
  - 1 KH
  - 1 NCC

👉 Không dùng dữ liệu production.

---

## IV. QUY TRÌNH TEST CHUẨN (THEO SỰ KIỆN)

### BƯỚC 1 – Test NHÁP (KHÔNG SINH SỐ)

- Tạo chứng từ ở trạng thái NHÁP
- Kiểm tra:
  - CORE có bản ghi
  - KHÔNG có:
    - nhật ký
    - snapshot
    - thay đổi báo cáo

👉 Có sinh số → FAIL

---

### BƯỚC 2 – Test XÁC NHẬN (SINH SỐ)

- Gọi API xác nhận
- Kiểm tra:
  - trạng thái chuyển đúng
  - nhật ký được sinh
  - số liệu thay đổi **đúng hướng**

👉 Sai hướng → FAIL

---

### BƯỚC 3 – Test HỦY / ĐIỀU CHỈNH

- Hủy chứng từ
- Kiểm tra:
  - không sinh số mới
  - không sửa số cũ
- Điều chỉnh:
  - phải tạo **chứng từ mới**

---

## V. CHECKLIST TEST THEO NGHIỆP VỤ

### 1. Nhập gas
- [ ] NHÁP không tăng kho
- [ ] XÁC NHẬN tăng kho
- [ ] CK sinh VAT đầu vào

### 2. Bán gas
- [ ] NHÁP không giảm kho
- [ ] XÁC NHẬN giảm kho
- [ ] Tiền vào đúng quỹ
- [ ] VAT đầu ra đúng

### 3. Thu – chi
- [ ] Không ảnh hưởng kho
- [ ] Đúng quỹ
- [ ] Công nợ đúng chiều

### 4. Thu ngân
- [ ] Giảm quỹ NV
- [ ] Tăng quỹ công ty
- [ ] KHÔNG sinh doanh thu

### 5. Kế toán – VAT
- [ ] VAT cân thuế không ảnh hưởng lợi nhuận
- [ ] Không gắn bán hàng

### 6. Báo cáo
- [ ] READ ONLY
- [ ] Không ghi DB
- [ ] So được CORE ↔ SNAPSHOT

---

## VI. TEST SNAPSHOT

- Chạy job chốt
- Kiểm tra:
  - snapshot khớp CORE
  - truncate + rebuild vẫn đúng

👉 Snapshot sai → lỗi CORE hoặc nhật ký.

---

## VII. TEST PHÂN QUYỀN

- NV:
  - không chốt
  - không xem báo cáo tài chính
- Kế toán:
  - chốt được
  - không sửa snapshot
- Admin:
  - toàn quyền

👉 Sai quyền = FAIL.

---

## VIII. QUY TRÌNH TRIỂN KHAI

1. Test PASS 100%
2. Freeze schema
3. Tag version API
4. Deploy
5. Theo dõi log 7 ngày đầu

❌ Không deploy khi chưa test đủ sự kiện.

---

## IX. QUẢN TRỊ

- File này là **CHUẨN TEST DUY NHẤT**
- Không test = không deploy
- Sai số = rollback ngay

---
