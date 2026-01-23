# CTVT3 – HỆ THỐNG QUẢN LÝ VẬN HÀNH CÔNG TY GAS

## 1. Giới thiệu

CTVT3 là hệ thống quản lý vận hành cho doanh nghiệp kinh doanh gas, được thiết kế với mục tiêu:

- số liệu đúng – nhất quán
- chống gian lận
- dễ kiểm toán
- mở rộng lâu dài
- không “đập hệ thống” khi phát triển thêm

Hệ thống được xây dựng theo tư duy **phân tầng chặt chẽ**, lấy dữ liệu làm trung tâm.

---

## 2. Triết lý thiết kế

- Dữ liệu chỉ có **1 nguồn sự thật**
- Ghi trước – chốt sau – đọc riêng
- Không sửa lịch sử
- Không trộn vai trò giữa các tầng
- Docs là luật, code phải tuân theo docs

---

## 3. Kiến trúc tổng thể (THEO LỚP)

┌──────────────────────────┐
│ MODULES │ API nghiệp vụ
├──────────────────────────┤
│ SYSTEM │ Auth – Permission – Audit – Chat
├──────────────────────────┤
│ MASTER │ Danh mục – không sinh số
├──────────────────────────┤
│ SNAPSHOT │ Chốt – báo cáo – read only
├──────────────────────────┤
│ JOURNAL │ Nhật ký – hệ quả
├──────────────────────────┤
│ CORE │ Transaction – nguồn sự thật
├──────────────────────────┤
│ COMMON │ Kỹ thuật dùng chung
└──────────────────────────┘

yaml
Sao chép mã

---

## 4. Vai trò các thư mục chính

### `docs/`
Não bộ hệ thống:
- nghiệp vụ
- quy tắc
- luồng xử lý
- hợp đồng API

👉 Code sai docs = code sai.

---

### `core/`
- sinh chứng từ gốc
- nguồn sự thật duy nhất
- không phụ thuộc module

---

### `journal/`
- ghi hệ quả từ core
- nhật ký kho, vỏ, chứng từ
- không API

---

### `snapshot/`
- dữ liệu chốt ngày
- báo cáo
- read only

---

### `master/`
- danh mục
- không sinh tiền
- không làm sai số

---

### `modules/`
- xử lý nghiệp vụ
- orchestration
- gọi core + system

---

### `system/`
- auth
- permission
- audit
- chat nội bộ

---

### `common/`
- kỹ thuật thuần
- exception
- utils
- validator
- decorator

---

## 5. Nguyên tắc phát triển

- Không viết tắt tầng
- Không bypass core
- Không sửa snapshot
- Không sửa journal
- Mọi nghiệp vụ mới phải có:
  - docs
  - rules
  - event

---

## 6. Trạng thái hiện tại

- Kiến trúc: ĐÃ CHỐT
- Database: ĐÃ CHỐT
- Common & System: ĐÃ KHÓA INTERFACE
- Sẵn sàng triển khai infra + API framework

---

## 7. Kết luận

CTVT3 không phải phần mềm CRUD đơn giản, mà là hệ thống vận hành.

Thiết kế đúng từ đầu → chạy bền 10–15 năm.  
Thiết kế sai → sửa mãi không xong.
