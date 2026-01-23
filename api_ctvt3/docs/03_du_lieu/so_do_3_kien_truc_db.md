# SƠ ĐỒ 3 – KIẾN TRÚC DATABASE HỆ THỐNG CTVT3
(BẢN CHUẨN CUỐI – DANH SÁCH BẢNG KHÔNG ĐƯỢC PHÁ)

---

## I. MỤC ĐÍCH

Sơ đồ này chốt **KIẾN TRÚC DATABASE CUỐI CÙNG** cho hệ thống CTVT3.

Trả lời 4 câu hỏi bắt buộc:
1. Hệ thống cần những bảng nào (CUỐI CÙNG)
2. Bảng nào là GỐC – bảng nào là PHỤ
3. Bảng nào được INSERT / UPDATE / KHÓA
4. API được phép tác động đến bảng nào

❗ Sau file này:
- Không thêm bảng cho “tiện”
- Không gộp bảng sai vai
- Không viết API vượt quyền DB

---

## II. PHÂN NHÓM DATABASE THEO VAI TRÒ

CTVT3 DB được chia thành **05 NHÓM BẢNG**:

A. CORE_GIAO_DICH  
B. NHAT_KY_HE_QUA  
C. CHOT_BAO_CAO  
D. DANH_MUC  
H. HE_THONG  

👉 Mỗi bảng **CHỈ ĐƯỢC PHÉP nằm trong 1 nhóm**.

---

## III. DANH SÁCH BẢNG CHUẨN THEO TỪNG NHÓM

---

### A. CORE_GIAO_DICH (BẢNG GỐC – NGUỒN SỰ THẬT)

**Danh sách bảng**

- hoa_don_ban  
- hoa_don_ban_chi_tiet  

- hoa_don_nhap  
- hoa_don_nhap_chi_tiet  

- thu_chi  
- thu_ngan  

- hoa_don_vat  
- gas_du  

**Quy tắc ghi**
- INSERT là chính
- UPDATE chỉ cho:
  - trạng thái
  - ghi chú
- KHÔNG DELETE cứng (chỉ hủy trạng thái)

👉 Thiếu 1 bảng CORE = sai nghiệp vụ.

---

### B. NHAT_KY_HE_QUA (KHÔNG NHẬP TAY)

**Danh sách bảng**
- nhat_ky_kho  
- nhat_ky_vo  

*(dự phòng tương lai: log_chung_tu)*

**Quy tắc**
- Chỉ sinh từ CORE
- Không API CRUD
- Không dùng làm nguồn tính

---

### C. CHOT_BAO_CAO (SNAPSHOT – ĐƯỢC XÓA)

**Danh sách bảng**
- ton_kho_chot  
- ton_kho_chot_ngay  

- gas_du_chot  
- gas_du_chot_ngay  

- quy_cong_ty_chot_ngay  
- quy_nhan_vien_chot_ngay  

**Quy tắc**
- Không INSERT tay
- Không UPDATE
- Có thể TRUNCATE và REBUILD

---

### D. DANH_MUC (MASTER DATA)

**Danh sách bảng**
- khach_hang  
- nha_cung_cap  
- nhan_vien  
- kho_hang  
- san_pham  
- nhan_vien_kho  

**Quy tắc**
- CRUD có kiểm soát
- Không chứa số dư / tồn / công nợ

---

### H. HE_THONG (KHÔNG LIÊN QUAN NGHIỆP VỤ)

**Danh sách bảng**
- user  
- user_role  
- user_permission  
- user_session  

- phong_chat  
- phong_chat_thanh_vien  
- tin_nhan  

- audit_log  

**Quy tắc**
- Không JOIN với CORE để tính số
- Không ảnh hưởng nghiệp vụ

---

## IV. QUYỀN GHI DB THEO TỪNG NHÓM

| Nhóm | INSERT | UPDATE | DELETE |
|----|-------|--------|--------|
| CORE_GIAO_DICH | ✅ | ⚠️ (trạng thái) | ❌ |
| NHAT_KY_HE_QUA | ❌ (auto) | ❌ | ❌ |
| CHOT_BAO_CAO | ❌ (job) | ❌ | ⚠️ (truncate) |
| DANH_MUC | ✅ | ✅ | ⚠️ |
| HE_THONG | ✅ | ✅ | ⚠️ |

---

## V. API ĐƯỢC PHÉP TÁC ĐỘNG ĐẾN ĐÂU

- API nghiệp vụ:
  → CHỈ ghi CORE_GIAO_DICH

- Service hệ quả:
  → ghi NHAT_KY_HE_QUA

- JOB hệ thống:
  → ghi CHOT_BAO_CAO

- API danh mục:
  → ghi DANH_MUC

- API hệ thống:
  → ghi HE_THONG

👉 API **KHÔNG ĐƯỢC** ghi chéo nhóm.

---

## VI. QUY TẮC CẤM TUYỆT ĐỐI

- Không bảng nào vừa là CORE vừa là SNAPSHOT
- Không tính số từ NHAT_KY / CHOT
- Không sửa số dư trực tiếp
- Không JOIN HE_THONG để tính kế toán

---

## VII. QUAN HỆ TỔNG QUÁT (DẠNG CHỮ)

[DANH_MUC]
    ↓
[CORE_GIAO_DICH]
    ↓
[NHAT_KY_HE_QUA]
    ↓
[CHOT_BAO_CAO]

[HE_THONG] bao ngoài – không chạm số

---

## VIII. QUẢN TRỊ TÀI LIỆU

- File này là **KIẾN TRÚC DB CUỐI**
- Đổi danh sách bảng = đổi toàn hệ thống
- Mọi thay đổi phải do ADMIN quyết định

---
