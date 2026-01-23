# KIẾN TRÚC CODE API CTVT3
(BẢN CHUẨN – KHÓA LOGIC – CHỐNG VỠ HỆ THỐNG)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **KIẾN TRÚC CODE CHUẨN** cho API CTVT3.

Mục tiêu:
1. Khóa vị trí đặt logic nghiệp vụ
2. Ngăn việc:
   - logic rơi vãi
   - service làm thay DB
   - controller tính toán
3. Đảm bảo code **phản chiếu đúng 5 sơ đồ**

👉 Đây là file để:
- review code
- onboard dev
- chặn phá kiến trúc

---

## II. NGUYÊN TẮC TỔNG QUÁT

1. **API chỉ đại diện cho sự kiện**
2. **Service là nơi duy nhất chứa nghiệp vụ**
3. **Repository không có logic**
4. **Không có code “tiện tay”**
5. **Không class nào được làm 2 vai**

---

## III. PHÂN LỚP KIẾN TRÚC (BẮT BUỘC)

CTVT3 chia code thành 6 lớp rõ ràng:

1. Controller (API Layer)
2. Service (Business Layer)
3. Core (Transaction Layer)
4. Journal (Hệ quả)
5. Snapshot (Chốt / báo cáo)
6. System & Common (bao ngoài)

---

## IV. CONTROLLER – LỚP API

**Vai trò**
- Nhận request
- Validate hình thức
- Gọi đúng Service

**ĐƯỢC PHÉP**
- parse input
- check quyền
- map request → DTO

**CẤM**
- tính tiền
- ghi DB trực tiếp
- sinh nhật ký
- sinh snapshot

👉 Controller **KHÔNG BIẾT KẾ TOÁN**

---

## V. SERVICE – TRÁI TIM NGHIỆP VỤ ⭐

**Vai trò**
- Thực thi nghiệp vụ
- Đại diện cho **SỰ KIỆN NGHIỆP VỤ**
- Quyết định:
  - khi nào sinh số
  - sinh cái gì

**ĐƯỢC PHÉP**
- ghi CORE_GIAO_DICH
- gọi service sinh nhật ký
- gọi job snapshot (gián tiếp)

**CẤM**
- đọc báo cáo để tính ngược
- sửa snapshot
- update số dư trực tiếp

👉 Mỗi Service = **1 hoặc vài sự kiện rõ ràng**

---

## VI. CORE – TRANSACTION LAYER

**Vai trò**
- Mapping 1–1 với bảng CORE_GIAO_DICH

**ĐẶC ĐIỂM**
- Không có logic nghiệp vụ
- Không gọi Service khác
- Chỉ chứa:
  - Entity
  - Repository

**QUY TẮC**
- Repository:
  - INSERT là chính
  - UPDATE chỉ trạng thái / ghi chú
  - KHÔNG tính toán

👉 CORE = **nguồn sự thật**

---

## VII. JOURNAL – HỆ QUẢ

**Vai trò**
- Ghi lại hậu quả phát sinh từ CORE

**ĐẶC ĐIỂM**
- Không có API
- Không nhập tay
- Sinh tự động

**LUỒNG**
Service nghiệp vụ  
→ gọi Journal Service  
→ ghi nhật ký

❌ Journal không bao giờ quyết định nghiệp vụ

---

## VIII. SNAPSHOT – CHỐT / BÁO CÁO

**Vai trò**
- Tạo ảnh chụp số liệu
- Phục vụ đọc nhanh

**ĐẶC ĐIỂM**
- Không có API ghi
- Có thể truncate
- Có thể rebuild

**QUY TẮC**
- Job chạy định kỳ
- Đọc CORE + JOURNAL
- Không logic nghiệp vụ

---

## IX. MASTER DATA – DANH MỤC

**Vai trò**
- Khai báo đối tượng

**QUY TẮC**
- CRUD có kiểm soát
- Không chứa số
- Không sinh hệ quả

👉 Danh mục **không phải nghiệp vụ**

---

## X. SYSTEM & COMMON – BAO NGOÀI

### System
- auth
- chat
- audit

❌ Không join CORE để tính số

### Common
- exception
- permission
- validator
- constant

👉 Common **không chứa nghiệp vụ**

---

## XI. LUỒNG CODE CHUẨN (DẠNG CHỮ)

Controller
↓
Service (nghiệp vụ)
↓
CORE (ghi giao dịch)
↓
Journal (ghi hệ quả)
↓
Snapshot Job (chốt)

yaml
Sao chép mã

❌ Không được đi ngược

---

## XII. CHECKLIST REVIEW CODE

Khi review 1 file, chỉ hỏi:

- File này thuộc lớp nào?
- Nó có làm đúng vai không?
- Có đụng việc của lớp khác không?
- Có sinh số ngoài Service không?

👉 Trả lời “có” sai → **REJECT**

---

## XIII. QUY TẮC KHÓA CUỐI

1. Không Service → không sinh số
2. Không sự kiện → không API
3. Không CORE → không có sự thật
4. Không snapshot → hệ thống vẫn chạy
5. Code phải phản ánh sơ đồ, không ngược lại

---

## XIV. QUẢN TRỊ

- File này là **HIẾN PHÁP KIẾN TRÚC CODE**
- Vi phạm = phá hệ thống
- Chỉ ADMIN được phép sửa