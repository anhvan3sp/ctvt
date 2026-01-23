# SYSTEM MODULE

## 1. Mục đích

`system/` là **hạ tầng lõi của toàn bộ hệ thống**, phục vụ cho:
- xác thực người dùng
- quản lý phiên làm việc
- phân quyền – kiểm soát truy cập
- ghi log kiểm toán
- các tiện ích hệ thống dùng chung

⚠️ **System KHÔNG chứa nghiệp vụ kinh doanh**  
⚠️ **System KHÔNG can thiệp logic kế toán, bán – nhập gas**

---

## 2. Nguyên tắc thiết kế

- System là tầng **nền**, mọi module khác phụ thuộc vào nó
- Không phụ thuộc ngược vào `modules/`, `master/`
- Code rõ ràng, dễ audit, dễ mở rộng
- Phân tách đúng vai trò:
  - Entity: mapping dữ liệu
  - Enum: chuẩn hoá trạng thái
  - Repository: CRUD thuần
  - Service: điều phối
  - Policy: kiểm tra quyền
  - Controller: điểm vào API

---

## 3. Cấu trúc thư mục

system/
│
├── auth/ # Xác thực – phiên làm việc
│
├── permission/ # Phân quyền – role – policy
│
├── audit/ # Log kiểm toán – truy vết
│
├── chat/ # Chat nội bộ (không nghiệp vụ)
│
└── enums/ # Enum dùng chung cho system

yaml
Sao chép mã

---

## 4. Auth – Xác thực & Phiên làm việc (`auth/`)

Chịu trách nhiệm:
- đăng nhập
- đăng xuất
- quản lý session
- quản lý token

### Thành phần:
- `entities/`  
  - User
  - UserSession
- `repositories/`  
  - UserRepo
  - SessionRepo
- `services/`  
  - AuthService
  - SessionService
- `controllers/`  
  - LoginController
  - LogoutController
- `enums/`  
  - TrangThaiUser
  - LoaiPhien

⚠️ Auth **không biết người dùng làm nghiệp vụ gì**

---

## 5. Permission – Phân quyền (`permission/`)

Chịu trách nhiệm:
- quản lý role
- quản lý permission
- kiểm tra quyền truy cập

### Thành phần:
- `entities/`
  - Role
  - Permission
  - RolePermission
- `repositories/`
  - RoleRepo
  - PermissionRepo
- `services/`
  - RoleService
  - PermissionService
- `policies/`
  - Policy theo nghiệp vụ (ban_gas, nhap_gas, ke_toan...)

⚠️ Policy **chỉ kiểm tra quyền**, không xử lý dữ liệu

---

## 6. Audit – Kiểm toán & truy vết (`audit/`)

Chịu trách nhiệm:
- ghi lại mọi hành động quan trọng
- phục vụ truy vết, kiểm tra gian lận
- không cho sửa lịch sử

### Thành phần:
- `entities/`
  - AuditLog
- `writers/`
  - AuditWriter
- `enums/`
  - LoaiHanhDong
  - DoiTuongTacDong

⚠️ Audit chỉ **ghi**, không đọc nghiệp vụ

---

## 7. Chat nội bộ (`chat/`)

Chức năng:
- chat nội bộ công ty
- trao đổi thông tin nhanh

⚠️ Chat:
- không sinh tiền
- không tác động sổ sách
- không ràng buộc nghiệp vụ

---

## 8. Enum chung (`system/enums/`)

Chứa các enum dùng chung:
- trạng thái phiên
- loại hệ thống (web / mobile / api)

⚠️ Enum system **được phép dùng ở mọi module**

---

## 9. Quan hệ với các module khác

modules/
↑
system/

markdown
Sao chép mã

- `modules/` **được phép gọi system**
- `system/` **KHÔNG BAO GIỜ gọi ngược modules**

---

## 10. Kết luận

- `system/` là **nền móng**
- Thiết kế sai system → cả hệ thống sai
- Thiết kế đúng system → mở rộng rất dễ

👉 Mọi thay đổi trong `system/` phải cân nhắc kỹ, tránh phá kiến trúc.
