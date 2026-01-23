# API CONTRACT – NGHIỆP VỤ KẾ TOÁN (VAT & CÂN THUẾ) – CTVT3
(BẢN CHUẨN – KHÓA DOANH THU & LỢI NHUẬN)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API** cho nghiệp vụ **KẾ TOÁN – VAT** trong CTVT3.

Mục tiêu:
1. Tách **VAT** ra khỏi **doanh thu** và **lợi nhuận**
2. Cho phép **cân thuế hợp pháp** mà không phá số vận hành
3. Ngăn tuyệt đối việc “đẻ doanh thu ảo” từ kế toán

---

## II. PHẠM VI NGHIỆP VỤ

Nghiệp vụ kế toán trong CTVT3 gồm 3 nhóm:

1. VAT phát sinh từ **bán hàng**
2. VAT phát sinh từ **nhập hàng**
3. VAT **cân thuế** (không gắn giao dịch thực)

👉 Cả 3 nhóm **đều ghi vào 1 bảng**: `hoa_don_vat`  
👉 Nhưng **KHÁC BẢN CHẤT**

---

## III. PHÂN LOẠI HÓA ĐƠN VAT

### 1. VAT ĐẦU RA (BÁN HÀNG)

- Nguồn sinh:
  - Hóa đơn bán **chuyển khoản**
- Bản chất:
  - Gắn với giao dịch bán
- Ảnh hưởng:
  - Tăng VAT phải nộp
  - KHÔNG tự sinh doanh thu

👉 Doanh thu đã sinh từ **hóa đơn bán**, không từ VAT.

---

### 2. VAT ĐẦU VÀO (NHẬP HÀNG)

- Nguồn sinh:
  - Hóa đơn nhập **chuyển khoản**
- Bản chất:
  - Thuế được khấu trừ
- Ảnh hưởng:
  - Tăng VAT đầu vào
  - VAT được cộng vào giá vốn tồn kho

---

### 3. VAT CÂN THUẾ ⭐ (NGHIỆP VỤ RIÊNG)

- Nguồn sinh:
  - Kế toán dịch vụ nhập tay
- Bản chất:
  - KHÔNG có giao dịch bán thật
- Ảnh hưởng:
  - Chỉ phục vụ báo cáo thuế

❌ KHÔNG:
- ảnh hưởng kho
- ảnh hưởng công nợ
- ảnh hưởng lợi nhuận NV

---

## IV. SỰ KIỆN NGHIỆP VỤ

| Sự kiện | Mã | Sinh số |
|------|----|--------|
| Ghi nhận VAT bán hàng | E6 | Có |
| Ghi nhận VAT nhập hàng | E6 | Có |
| Ghi nhận VAT cân thuế | E7 | Có |

---

## V. DANH SÁCH API

---

### 1. GHI NHẬN VAT CÂN THUẾ ⭐

**Endpoint**
POST /ke-toan/can-thue

yaml
Sao chép mã

**Mục đích**
- Tạo hóa đơn VAT **không gắn giao dịch bán**

**Ghi DB**
- hoa_don_vat
  - loai = can_thue
  - bang_tham_chieu = NULL
  - id_tham_chieu = NULL

---

### 2. Cập nhật VAT (NHÁP – nếu cho phép)

> Chỉ ADMIN / KẾ TOÁN ONLINE

PUT /ke-toan/vat/{id}

yaml
Sao chép mã

❌ Không được đổi loại VAT  
❌ Không được gắn giao dịch bán

---

### 3. GHI NHẬN THUẾ ⭐

POST /ke-toan/vat/{id}/ghi-nhan

yaml
Sao chép mã

**Đại diện sự kiện**
- E6 hoặc E7

**Hành vi**
- Chuyển trạng thái → ĐÃ GHI NHẬN THUẾ

---

## VI. QUY TẮC GHI DB (KHÓA CỨNG)

API kế toán:
- ✅ CHỈ ghi `hoa_don_vat`
- ❌ KHÔNG ghi:
  - hoa_don_ban
  - hoa_don_nhap
  - thu_chi
  - thu_ngan
  - nhật ký kho

👉 VAT **KHÔNG BAO GIỜ** là nguồn sinh doanh thu.

---

## VII. ẢNH HƯỞNG NGHIỆP VỤ

| Thành phần | VAT bán | VAT nhập | VAT cân thuế |
|----------|---------|----------|--------------|
| Kho | ❌ | ❌ | ❌ |
| Quỹ | ❌ | ❌ | ❌ |
| Công nợ | ❌ | ❌ | ❌ |
| Doanh thu | ❌ | ❌ | ❌ |
| Lợi nhuận NV | ❌ | ❌ | ❌ |
| Thuế phải nộp | ✅ | ❌ | ✅ |

---

## VIII. NHỮNG ĐIỀU BỊ CẤM TUYỆT ĐỐI

- Tạo VAT để sinh doanh thu
- Gắn VAT cân thuế vào hóa đơn bán
- Lấy VAT làm nguồn tính lợi nhuận
- API kế toán ghi bảng CORE khác

👉 Vi phạm = phá hệ thống

---

## IX. CHECKLIST REVIEW API KẾ TOÁN

- VAT có gắn bán hàng thật không?
- VAT cân thuế có ảnh hưởng lợi nhuận không?
- API có ghi bảng khác ngoài hoa_don_vat không?

👉 Có → **API SAI**

---

## X. QUẢN TRỊ

- VAT = nghĩa vụ thuế, không phải doanh thu
- File này là **KHÓA KẾ TOÁN**
- Sửa file này = sửa toàn hệ thống
