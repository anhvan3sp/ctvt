# API CONTRACT – NGHIỆP VỤ NHẬP GAS (CTVT3)
(BẢN CHUẨN – KHÔNG CODE – KHÔNG TÍNH)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API** cho nghiệp vụ **NHẬP GAS** trong hệ thống CTVT3.

API contract dùng để:
1. Khóa trách nhiệm API nhập gas
2. Đảm bảo API chỉ đại diện cho **SỰ KIỆN NGHIỆP VỤ**
3. Ngăn việc:
   - API tự cộng tồn kho
   - API tự ghi công nợ
   - API tự xử lý VAT sai ngữ cảnh

---

## II. NGHIỆP VỤ GỐC

- Nghiệp vụ: **NHẬP GAS**
- Sự kiện nghiệp vụ: **E1 – XÁC NHẬN HÓA ĐƠN NHẬP GAS**
- Thời điểm sinh số: khi hóa đơn chuyển sang **ĐÃ GHI NHẬN**

---

## III. DANH SÁCH API

### 1. Tạo hóa đơn nhập (NHÁP)

**Endpoint**
POST /nhap-gas/hoa-don

markdown
Sao chép mã

**Mục đích**
- Tạo hóa đơn nhập ở trạng thái **NHÁP**
- Chưa sinh số

**Ghi DB**
- hoa_don_nhap (status = NHÁP)

❌ KHÔNG:
- tăng tồn kho
- sinh công nợ
- sinh VAT
- ảnh hưởng quỹ

---

### 2. Thêm chi tiết hóa đơn nhập

**Endpoint**
POST /nhap-gas/hoa-don/{id}/chi-tiet

yaml
Sao chép mã

**Mục đích**
- Ghi chi tiết gas / vỏ / kg nhập

**Ghi DB**
- hoa_don_nhap_chi_tiet

❌ KHÔNG sinh số

---

### 3. Cập nhật thông tin NHÁP

**Endpoint**
PUT /nhap-gas/hoa-don/{id}

yaml
Sao chép mã

**Điều kiện**
- Chỉ cho phép khi trạng thái = NHÁP

**Ghi DB**
- hoa_don_nhap (ghi chú, metadata)

❌ KHÔNG sinh số

---

### 4. XÁC NHẬN HÓA ĐƠN NHẬP ⭐

**Endpoint**
POST /nhap-gas/hoa-don/{id}/xac-nhan

yaml
Sao chép mã

**MỤC ĐÍCH**
- Đại diện cho **SỰ KIỆN E1**
- Là **API DUY NHẤT** được phép sinh số cho nhập gas

---

## IV. HÀNH VI KHI XÁC NHẬN (KHÓA CỨNG)

### 1. Điều kiện bắt buộc

- Hóa đơn tồn tại
- Trạng thái = NHÁP
- Người gọi API có quyền xác nhận
- Có ít nhất 1 dòng chi tiết
- Nhà cung cấp hợp lệ

❌ Sai 1 điều → reject

---

### 2. Ghi DB (CORE_GIAO_DICH)

Khi xác nhận thành công, API **CHỈ ĐƯỢC PHÉP**:

**Ghi / cập nhật**
- hoa_don_nhap
  - trạng thái → ĐÃ GHI NHẬN
- hoa_don_nhap_chi_tiet (đã có)

**Có thể ghi thêm**
- hoa_don_vat (nếu nhập chuyển khoản)
- gas_du (nếu có gas dư trả NCC)

👉 API **KHÔNG**:
- ghi tồn kho
- ghi công nợ
- ghi quỹ

---

### 3. Sinh hệ quả (TỰ ĐỘNG – SAU CORE)

Sau khi ghi CORE:
- Sinh nhat_ky_kho (nhập)
- Sinh nhat_ky_vo (nếu có)

👉 Nhật ký **không do API ghi trực tiếp**

---

## V. ẢNH HƯỞNG NGHIỆP VỤ (ĐỂ ĐỐI SOÁT)

Sau khi xác nhận, hệ thống **PHẢI ĐẢM BẢO**:

- Tăng tồn kho gas
- Phát sinh công nợ nhà cung cấp
- Giảm quỹ:
  - quỹ công ty (nếu thanh toán)
  - quỹ nhân viên (nếu ứng tiền)
- Phát sinh VAT đầu vào (nếu CK)

❗ Các ảnh hưởng này **KHÔNG do API tính**  
❗ Chỉ dùng để kiểm tra logic

---

## VI. NHỮNG ĐIỀU BỊ CẤM TUYỆT ĐỐI

- API cộng tồn kho
- API cập nhật công nợ NCC
- API cập nhật quỹ
- API ghi snapshot
- API tính báo cáo

---

## VII. CHECKLIST REVIEW API NHẬP GAS

- Có đại diện đúng sự kiện E1 không?
- Sinh số đúng thời điểm xác nhận chưa?
- Ghi đúng bảng CORE chưa?
- Có logic “tính hộ” nào không?

👉 Có → **LOẠI**

---

## VIII. QUẢN TRỊ

- File này là **HỢP ĐỒNG API**
- Sửa file này = sửa toàn bộ luồng nhập
- Mọi thay đổi phải do ADMIN quyết định

---