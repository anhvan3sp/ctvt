# API CONTRACT – BÁO CÁO & ĐỐI SOÁT (CTVT3)
(BẢN CHUẨN – READ ONLY – KHÓA GHI DB)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API BÁO CÁO** cho hệ thống CTVT3.

Mục tiêu:
1. Chuẩn hóa API **CHỈ ĐỌC**
2. Ngăn tuyệt đối việc:
   - tính ngược số liệu
   - sửa số qua báo cáo
3. Khóa logic:  
   **BÁO CÁO ≠ NGUỒN SỰ THẬT**

---

## II. NGUYÊN TẮC CỐT LÕI

1. Báo cáo **KHÔNG PHẢI** nghiệp vụ
2. Báo cáo **KHÔNG SINH SỐ**
3. Báo cáo **KHÔNG GHI CORE**
4. Báo cáo **KHÔNG GHI NHẬT KÝ**
5. Báo cáo **KHÔNG GHI SNAPSHOT**

👉 Báo cáo chỉ đọc dữ liệu đã hợp lệ.

---

## III. NGUỒN DỮ LIỆU ĐƯỢC PHÉP ĐỌC

API báo cáo **CHỈ ĐƯỢC READ** từ:

- CORE_GIAO_DICH (đã ĐÃ GHI NHẬN / ĐÃ CHỐT)
- NHAT_KY_HE_QUA (đối soát)
- CHOT_BAO_CAO (ưu tiên đọc nhanh)

❌ KHÔNG:
- INSERT
- UPDATE
- DELETE
- CALL JOB

---

## IV. DANH SÁCH API BÁO CÁO

---

### 1. BÁO CÁO CÔNG NỢ

GET /bao-cao/cong-no

markdown
Sao chép mã

**Nội dung**
- Công nợ khách hàng
- Công nợ nhà cung cấp
- Tách:
  - tiền
  - vỏ

**Nguồn**
- CORE_GIAO_DICH
- NHAT_KY_VO

❌ Không ghi DB

---

### 2. BÁO CÁO TỒN KHO

GET /bao-cao/ton-kho

yaml
Sao chép mã

**Nội dung**
- Tồn kho theo kho / sản phẩm
- Tổng nhập
- Tổng xuất
- Chênh lệch

**Nguồn**
- ton_kho_chot_ngay (ưu tiên)
- nhat_ky_kho (đối soát)

---

### 3. BÁO CÁO LỢI NHUẬN NHÂN VIÊN

GET /bao-cao/loi-nhuan

yaml
Sao chép mã

**Nội dung**
- Doanh số bán
- Giá nhận
- Chênh lệch
- Theo ngày / tháng

❌ KHÔNG tính VAT  
❌ KHÔNG lấy từ hoa_don_vat

---

### 4. BÁO CÁO VAT

GET /bao-cao/vat

yaml
Sao chép mã

**Nội dung**
- VAT đầu vào
- VAT đầu ra
- VAT cân thuế
- VAT phải nộp

**Nguồn**
- hoa_don_vat (READ ONLY)

---

### 5. BÁO CÁO QUỸ

GET /bao-cao/quy

yaml
Sao chép mã

**Nội dung**
- Quỹ công ty:
  - tiền mặt
  - chuyển khoản
- Quỹ nhân viên

**Nguồn**
- thu_chi
- thu_ngan
- quy_cong_ty_chot_ngay
- quy_nhan_vien_chot_ngay

---

## V. QUY TẮC ĐỐI SOÁT

Báo cáo phải cho phép:
- So snapshot ↔ CORE
- So snapshot ↔ nhật ký
- Phát hiện:
  - lệch kho
  - lệch tiền
  - lệch công nợ

👉 Báo cáo **không sửa**, chỉ **phát hiện**.

---

## VI. NHỮNG API BỊ CẤM TUYỆT ĐỐI

- POST /bao-cao/*
- PUT /bao-cao/*
- DELETE /bao-cao/*
- API rebuild snapshot
- API chỉnh số báo cáo

👉 Nếu cần điều chỉnh → **tạo chứng từ mới**

---

## VII. CHECKLIST REVIEW API BÁO CÁO

- API có ghi DB không?
- API có gọi job không?
- API có update snapshot không?
- API có tính ngược từ báo cáo không?

👉 Có → **API SAI – CẤM TRIỂN KHAI**

---

## VIII. QUẢN TRỊ

- Báo cáo = kính soi
- Không phải tay chỉnh
- File này là **KHÓA GHI CUỐI CÙNG**
