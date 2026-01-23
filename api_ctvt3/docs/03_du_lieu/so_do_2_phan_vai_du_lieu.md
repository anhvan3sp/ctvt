# SƠ ĐỒ 2B – PHÂN VAI DỮ LIỆU HỆ THỐNG CTVT3
(BẢN CHUẨN CUỐI – KHÓA VAI TRÒ BẢNG)

---

## I. MỤC ĐÍCH

Tài liệu này dùng để **phân vai tuyệt đối cho từng bảng dữ liệu**  
trong hệ thống CTVT3, nhằm:

1. Xác định bảng nào là **NGUỒN SỰ THẬT**
2. Ngăn DB và API làm sai nghiệp vụ
3. Cấm tuyệt đối các hành vi:
   - dùng bảng sai vai
   - tính ngược từ bảng không phải gốc
   - vừa ghi vừa báo cáo trong cùng bảng

👉 Mỗi bảng **CHỈ ĐƯỢC PHÉP có 1 vai trò duy nhất**.

---

## II. NGUYÊN TẮC PHÂN VAI TỔNG QUÁT

CTVT3 có **05 LỚP DỮ LIỆU**, áp dụng cho TOÀN BỘ hệ thống:

1. **LỚP A – CORE_GIAO_DICH**  
2. **LỚP B – NHAT_KY_HE_QUA**  
3. **LỚP C – CHOT_BAO_CAO (SNAPSHOT)**  
4. **LỚP D – DANH_MUC (MASTER DATA)**  
5. **LỚP H – HE_THONG**

👉 Không tồn tại lớp thứ 6.  
👉 Không bảng nào được đứng 2 lớp.

---

## III. LỚP A – CORE_GIAO_DỊCH (NGUỒN SỰ THẬT)

### 1. Bản chất
- Mỗi dòng = **1 sự kiện nghiệp vụ đã được ghi nhận**
- Là **nguồn duy nhất** sinh:
  - tiền
  - kho
  - công nợ
  - VAT

### 2. Danh sách bảng

- hoa_don_ban  
- hoa_don_ban_chi_tiet  

- hoa_don_nhap  
- hoa_don_nhap_chi_tiet  

- thu_chi  
- thu_ngan  

- hoa_don_vat  
- gas_du  

### 3. Quy tắc bất di bất dịch
- INSERT là chính
- UPDATE chỉ cho:
  - trạng thái
  - ghi chú
- KHÔNG xóa cứng
- KHÔNG tính ngược từ bảng khác

👉 **Sai CORE = sai toàn hệ thống**

---

## IV. LỚP B – NHẬT KÝ HỆ QUẢ (KHÔNG NHẬP TAY)

### 1. Bản chất
- Ghi lại **hậu quả phát sinh từ CORE**
- Dùng cho:
  - truy vết
  - đối soát
  - kiểm toán

### 2. Danh sách bảng

- nhat_ky_kho  
- nhat_ky_vo  
- (tương lai) log_chung_tu  

### 3. Quy tắc
- CHỈ sinh tự động từ CORE
- CẤM:
  - nhập tay
  - sửa tay
  - dùng làm nguồn tính

👉 Nhật ký **chỉ ghi – không tính**

---

## V. LỚP C – CHỐT / BÁO CÁO (SNAPSHOT)

### 1. Bản chất
- Ảnh chụp số liệu tại một thời điểm
- Phục vụ đọc nhanh – báo cáo

### 2. Danh sách bảng

- ton_kho_chot  
- ton_kho_chot_ngay  

- gas_du_chot  
- gas_du_chot_ngay  

- quy_cong_ty_chot_ngay  
- quy_nhan_vien_chot_ngay  

### 3. Quy tắc
- Không INSERT tay
- Không UPDATE
- Được TRUNCATE / REBUILD
- KHÔNG bao giờ là nguồn sự thật

👉 Snapshot **có thể sai – CORE không được sai**

---

## VI. LỚP D – DANH MỤC (MASTER DATA)

### 1. Bản chất
- Đối tượng tham gia nghiệp vụ
- Không tự sinh số liệu

### 2. Danh sách bảng

- khach_hang  
- nha_cung_cap  
- nhan_vien  
- kho_hang  
- san_pham  
- nhan_vien_kho  

### 3. Quy tắc
- CRUD có kiểm soát
- Không chứa:
  - số dư
  - tồn kho
  - công nợ

👉 Danh mục **KHÔNG BAO GIỜ là giao dịch**

---

## VII. LỚP H – HỆ THỐNG (BAO NGOÀI)

### 1. Bản chất
- Phục vụ vận hành phần mềm
- Không tồn tại trong kế toán ngoài đời

### 2. Danh sách bảng

- user  
- user_role  
- user_permission  
- user_session  

- phong_chat  
- phong_chat_thanh_vien  
- tin_nhan  

- audit_log  

### 3. Quy tắc
- Không JOIN với CORE để tính số
- Không ảnh hưởng nghiệp vụ
- Chỉ kiểm soát quyền truy cập

👉 Hệ thống **không bao giờ được đụng số**

---

## VIII. QUY TẮC VÀNG KIỂM TRA NHANH

Chỉ cần hỏi:
> **“Bảng này thuộc lớp nào?”**

- Trả lời được → đúng
- Ấp úng → sai thiết kế

---

## IX. QUAN HỆ TỔNG QUÁT (DẠNG CHỮ)

[DANH_MUC]
    ↓
[CORE_GIAO_DICH]
    ↓
[NHAT_KY_HE_QUA]
    ↓
[CHOT_BAO_CAO]

[HE_THONG] bao ngoài – không chạm số

---

## X. QUẢN TRỊ TÀI LIỆU

- File này khóa **vai trò dữ liệu**
- Đổi vai 1 bảng = phá kiến trúc
- Mọi thay đổi phải do ADMIN quyết định

---
