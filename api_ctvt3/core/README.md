# CORE TRANSACTION – NGUỒN SỰ THẬT (CTVT3)

## 1. VAI TRÒ CORE

CORE là lớp:
- Ghi nhận giao dịch gốc
- Là NGUỒN SỰ THẬT DUY NHẤT sinh số liệu

Mọi số liệu:
- tồn kho
- quỹ
- công nợ
- VAT

ĐỀU PHẢI xuất phát từ CORE.

---

## 2. NGUYÊN TẮC BẤT DI BẤT DỊCH

1. CORE chỉ ghi nhận SỰ KIỆN NGHIỆP VỤ
2. CORE không tổng hợp
3. CORE không tính toán báo cáo
4. CORE không cập nhật số dư
5. CORE không được đọc snapshot để tính ngược
6. CORE không được sửa số đã ghi nhận
7. Điều chỉnh số liệu = tạo giao dịch mới

---

## 3. CẤU TRÚC CORE

core/
├── entities/        # Mapping bảng DB – không logic


Không có:
- service nghiệp vụ
- rules
- validators

---

## 4. DANH SÁCH BẢNG CORE

- hoa_don_ban
- hoa_don_ban_chi_tiet
- hoa_don_nhap
- hoa_don_nhap_chi_tiet
- thu_chi
- thu_ngan
- hoa_don_vat
- gas_du

---

## 5. QUY TẮC CODE

### Entities
- Mapping 1–1 với bảng DB
- Không có method nghiệp vụ
- Không tính toán
- Không side-effect

### Repositories
- Chỉ CRUD
- Không kiểm quyền
- Không sinh nghiệp vụ
- Không gọi journal
- Không gọi snapshot

---

## 6. NHỮNG ĐIỀU BỊ CẤM

- update tồn kho
- update công nợ
- update quỹ
- tính báo cáo
- join snapshot
CORE là lõi nghiệp vụ của hệ thống CTVT3.

CORE chỉ mô tả:
- đối tượng nghiệp vụ
- trạng thái
- luật bất biến

CORE KHÔNG:
- ghi hoặc đọc database
- xử lý API
- xử lý HTTP
- chứa repository hoặc SQL

Mọi nghiệp vụ thực thi nằm ngoài CORE.


Vi phạm README này = PHÁ KIẾN TRÚC CTVT3.
