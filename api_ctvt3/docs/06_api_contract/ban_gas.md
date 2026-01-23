# API CONTRACT – NGHIỆP VỤ BÁN GAS (CTVT3)
(BẢN CHUẨN – KHÔNG CODE – KHÔNG TÍNH)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API** cho nghiệp vụ **BÁN GAS** trong hệ thống CTVT3.

API contract dùng để:
1. Khóa phạm vi trách nhiệm của API
2. Đảm bảo API chỉ đại diện cho **SỰ KIỆN NGHIỆP VỤ**
3. Ngăn việc:
   - API tự tính kế toán
   - API sửa số
   - API ghi sai bảng

👉 File này là **cam kết giữa nghiệp vụ – DB – code**.

---

## II. NGHIỆP VỤ GỐC

- Nghiệp vụ: **BÁN GAS**
- Sự kiện nghiệp vụ: **E2 – XÁC NHẬN HÓA ĐƠN BÁN GAS**
- Thời điểm sinh số: khi hóa đơn chuyển sang **ĐÃ GHI NHẬN**

---

## III. DANH SÁCH API

### 1. Tạo hóa đơn bán (NHÁP)

**Endpoint**
POST /ban-gas/hoa-don

markdown
Sao chép mã

**Mục đích**
- Tạo hóa đơn bán ở trạng thái **NHÁP**
- Chưa sinh số

**Ghi DB**
- hoa_don_ban (status = NHÁP)

❌ KHÔNG:
- sinh tồn kho
- sinh tiền
- sinh công nợ
- sinh VAT

---

### 2. Thêm chi tiết hóa đơn

**Endpoint**
POST /ban-gas/hoa-don/{id}/chi-tiet

yaml
Sao chép mã

**Mục đích**
- Ghi chi tiết bán gas / vỏ / kg

**Ghi DB**
- hoa_don_ban_chi_tiet

❌ KHÔNG sinh số

---

### 3. Cập nhật thông tin NHÁP

**Endpoint**
PUT /ban-gas/hoa-don/{id}

yaml
Sao chép mã

**Điều kiện**
- Chỉ cho phép khi trạng thái = NHÁP

**Ghi DB**
- hoa_don_ban (ghi chú, metadata)

❌ KHÔNG sinh số

---

### 4. XÁC NHẬN HÓA ĐƠN BÁN ⭐

**Endpoint**
POST /ban-gas/hoa-don/{id}/xac-nhan

yaml
Sao chép mã

**MỤC ĐÍCH**
- Đại diện cho **SỰ KIỆN E2**
- Là **API DUY NHẤT** được phép sinh số cho bán gas

---

## IV. HÀNH VI KHI XÁC NHẬN (KHÓA CỨNG)

### 1. Điều kiện bắt buộc

- Hóa đơn tồn tại
- Trạng thái = NHÁP
- Người gọi API có quyền xác nhận
- Dữ liệu chi tiết hợp lệ

❌ Sai 1 điều → reject

---

### 2. Ghi DB (CORE_GIAO_DICH)

Khi xác nhận thành công, API **CHỈ ĐƯỢC PHÉP**:

**Ghi / cập nhật**
- hoa_don_ban
  - trạng thái → ĐÃ GHI NHẬN
- hoa_don_ban_chi_tiet (đã có)

**Có thể ghi thêm**
- gas_du (nếu bán theo kg)
- hoa_don_vat (nếu phát sinh VAT)

👉 API **KHÔNG**:
- ghi tồn kho
- ghi công nợ
- ghi quỹ

---

### 3. Sinh hệ quả (TỰ ĐỘNG – SAU CORE)

Sau khi ghi CORE:
- Sinh nhat_ky_kho (xuất)
- Sinh nhat_ky_vo (nếu có)

👉 Nhật ký **không do API ghi trực tiếp**

---

## V. ẢNH HƯỞNG NGHIỆP VỤ (ĐỂ ĐỐI SOÁT)

Sau khi xác nhận, hệ thống **PHẢI ĐẢM BẢO**:

- Giảm tồn kho (tính từ CORE + nhật ký)
- Tăng tiền:
  - tiền mặt → quỹ nhân viên
  - chuyển khoản → quỹ công ty
- Phát sinh công nợ khách (nếu bán thiếu)
- Phát sinh VAT đầu ra (nếu CK)

❗ Các ảnh hưởng này **KHÔNG do API tính**  
❗ Chỉ dùng để kiểm tra logic

---

## VI. NHỮNG ĐIỀU BỊ CẤM TUYỆT ĐỐI

- API cập nhật tồn kho
- API cập nhật công nợ
- API cập nhật quỹ
- API ghi snapshot
- API tính báo cáo

👉 Vi phạm = API SAI.

---

## VII. CHECKLIST REVIEW API BÁN GAS

Khi review, chỉ cần hỏi:

- API này có đại diện cho E2 không?
- Sinh số có đúng lúc xác nhận không?
- Ghi đúng bảng CORE chưa?
- Có dòng code nào “tính cho tiện” không?

👉 Có → **LOẠI**

---

## VIII. QUẢN TRỊ

- File này là **HỢP ĐỒNG API**
- Mọi sửa đổi phải do ADMIN quyết định
- Sửa contract = sửa code + DB liên quan

---