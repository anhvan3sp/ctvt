# API CONTRACT – NGHIỆP VỤ THU / CHI (CTVT3)
(BẢN CHUẨN – KHÔNG CODE – KHÔNG TÍNH)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API** cho nghiệp vụ **THU – CHI PHÁT SINH**
trong hệ thống CTVT3.

Mục tiêu:
1. Chuẩn hóa cách ghi **phiếu thu / phiếu chi**
2. Giảm tải cho nghiệp vụ kế toán
3. Ngăn tuyệt đối:
   - cập nhật quỹ bằng tay
   - cập nhật công nợ trực tiếp
   - dùng thu/chi để “vá số”

---

## II. PHẠM VI NGHIỆP VỤ

Nghiệp vụ THU / CHI dùng cho:
- Chi phí phát sinh ngoài hóa đơn
- Thu / chi liên quan đặt hàng
- Ứng tiền / hoàn tiền
- Điều chỉnh dòng tiền **không qua bán / nhập**

❌ KHÔNG dùng cho:
- Bán gas
- Nhập gas
- Thu ngân (NV nộp tiền)

---

## III. NGHIỆP VỤ GỐC

- Nghiệp vụ: **THU – CHI PHÁT SINH**
- Sự kiện nghiệp vụ:
  - **E3 – GHI NHẬN PHIẾU THU**
  - **E4 – GHI NHẬN PHIẾU CHI**
- Thời điểm sinh số: khi phiếu chuyển sang **ĐÃ GHI NHẬN**

---

## IV. DANH SÁCH API

---

### 1. Lập phiếu THU (NHÁP)

**Endpoint**
POST /thu-chi/thu

yaml
Sao chép mã

**Mục đích**
- Lập phiếu thu ở trạng thái **NHÁP**

**Ghi DB**
- thu_chi (loai = THU, status = NHÁP)

❌ KHÔNG:
- tăng quỹ
- giảm công nợ
- sinh VAT

---

### 2. Lập phiếu CHI (NHÁP)

**Endpoint**
POST /thu-chi/chi

yaml
Sao chép mã

**Mục đích**
- Lập phiếu chi ở trạng thái **NHÁP**

**Ghi DB**
- thu_chi (loai = CHI, status = NHÁP)

❌ KHÔNG:
- giảm quỹ
- tăng công nợ
- sinh VAT

---

### 3. Cập nhật phiếu THU / CHI (NHÁP)

**Endpoint**
PUT /thu-chi/{id}

yaml
Sao chép mã

**Điều kiện**
- Chỉ cho phép khi trạng thái = NHÁP

**Ghi DB**
- thu_chi (ghi chú, thông tin phụ)

❌ KHÔNG sinh số

---

### 4. XÁC NHẬN PHIẾU THU / CHI ⭐

**Endpoint**
POST /thu-chi/{id}/xac-nhan

yaml
Sao chép mã

**MỤC ĐÍCH**
- Đại diện cho **SỰ KIỆN E3 hoặc E4**
- Là **API DUY NHẤT** được phép sinh số cho thu/chi

---

## V. HÀNH VI KHI XÁC NHẬN (KHÓA CỨNG)

### 1. Điều kiện bắt buộc

- Phiếu tồn tại
- Trạng thái = NHÁP
- Người gọi có quyền xác nhận
- Xác định rõ:
  - thu hay chi
  - nguồn tiền
  - đối tượng liên quan (nếu có)

❌ Thiếu → reject

---

### 2. Ghi DB (CORE_GIAO_DICH)

Khi xác nhận, API **CHỈ ĐƯỢC PHÉP**:

- Cập nhật thu_chi:
  - trạng thái → ĐÃ GHI NHẬN

**Có thể ghi thêm**
- hoa_don_vat (nếu phát sinh VAT)

👉 API **KHÔNG**:
- cập nhật quỹ
- cập nhật công nợ
- cập nhật tồn kho

---

### 3. Sinh hệ quả (TỰ ĐỘNG)

Sau khi ghi CORE:
- Hệ thống tự phản ánh:
  - tăng / giảm quỹ
  - tăng / giảm công nợ (nếu liên quan)

👉 **Không có bảng CORE riêng cho quỹ / công nợ**

---

## VI. ẢNH HƯỞNG NGHIỆP VỤ (ĐỂ ĐỐI SOÁT)

### Phiếu THU
- Tăng quỹ NV hoặc quỹ công ty
- Giảm công nợ khách (hoặc âm nếu thu trước)

### Phiếu CHI
- Giảm quỹ
- Tăng công nợ NCC (nếu liên quan)

❗ Không do API tính  
❗ Chỉ để kiểm tra logic

---

## VII. NHỮNG ĐIỀU BỊ CẤM TUYỆT ĐỐI

- Dùng thu/chi để sửa sai bán / nhập
- API ghi quỹ
- API ghi công nợ
- API ghi snapshot
- API tính báo cáo

---

## VIII. CHECKLIST REVIEW API THU / CHI

- Có đại diện đúng E3 / E4 không?
- Sinh số đúng lúc xác nhận không?
- Có “update quỹ” trong code không?
- Có lạm dụng thu/chi không?

👉 Có → **LOẠI**

---

## IX. QUẢN TRỊ

- File này là **HỢP ĐỒNG API**
- Lạm dụng thu/chi = phá kế toán
- Mọi thay đổi phải do ADMIN quyết định
