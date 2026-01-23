# API CONTRACT – NGHIỆP VỤ THU NGÂN (CTVT3)
(BẢN CHUẨN – KHÓA DOANH THU – KHÔNG ĐƯỢC SAI)

---

## I. MỤC ĐÍCH

Tài liệu này định nghĩa **HỢP ĐỒNG API** cho nghiệp vụ **THU NGÂN**  
( NHÂN VIÊN NỘP TIỀN VỀ CÔNG TY ).

Mục tiêu:
1. Phân biệt rõ **thu ngân ≠ thu tiền bán hàng**
2. Khóa tuyệt đối việc ghi nhận doanh thu sai
3. Chuẩn hóa luồng dịch chuyển tiền nội bộ

---

## II. BẢN CHẤT NGHIỆP VỤ

**Thu ngân là gì?**

- Là việc **nhân viên nộp lại tiền** đã thu từ khách
- Là **dịch chuyển tiền nội bộ**
- KHÔNG phải là nghiệp vụ tạo doanh thu

👉 Thu ngân **KHÔNG BAO GIỜ**:
- tạo hóa đơn bán
- tạo doanh thu
- tạo VAT
- ảnh hưởng lợi nhuận

---

## III. NGHIỆP VỤ GỐC

- Nghiệp vụ: **THU NGÂN**
- Chứng từ: **Phiếu nộp tiền**
- Sự kiện nghiệp vụ: **E5 – GHI NHẬN PHIẾU THU NGÂN**
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN**

---

## IV. DANH SÁCH API

---

### 1. Lập phiếu THU NGÂN (NHÁP)

**Endpoint**
POST /thu-ngan/nop-tien

yaml
Sao chép mã

**Mục đích**
- Lập phiếu nộp tiền ở trạng thái **NHÁP**

**Ghi DB**
- thu_ngan (status = NHÁP)

❌ KHÔNG:
- tăng quỹ công ty
- giảm quỹ nhân viên
- sinh doanh thu

---

### 2. Cập nhật phiếu THU NGÂN (NHÁP)

**Endpoint**
PUT /thu-ngan/{id}

yaml
Sao chép mã

**Điều kiện**
- Chỉ cho phép khi trạng thái = NHÁP

**Ghi DB**
- thu_ngan (ghi chú)

❌ KHÔNG sinh số

---

### 3. XÁC NHẬN PHIẾU THU NGÂN ⭐

**Endpoint**
POST /thu-ngan/{id}/xac-nhan

yaml
Sao chép mã

**MỤC ĐÍCH**
- Đại diện cho **SỰ KIỆN E5**
- Là **API DUY NHẤT** được phép sinh số cho thu ngân

---

## V. HÀNH VI KHI XÁC NHẬN (KHÓA CỨNG)

### 1. Điều kiện bắt buộc

- Phiếu tồn tại
- Trạng thái = NHÁP
- Có nhân viên nộp tiền
- Có số tiền hợp lệ
- Người xác nhận có quyền

❌ Thiếu → reject

---

### 2. Ghi DB (CORE_GIAO_DICH)

Khi xác nhận:
- Cập nhật thu_ngan:
  - trạng thái → ĐÃ GHI NHẬN

👉 API **CHỈ** được phép ghi bảng `thu_ngan`

---

### 3. Sinh hệ quả (TỰ ĐỘNG – NGOÀI API)

Sau khi xác nhận:
- Giảm quỹ nhân viên
- Tăng quỹ công ty

👉 Không có bảng quỹ gốc  
👉 Không có API ghi quỹ

---

## VI. ẢNH HƯỞNG NGHIỆP VỤ (ĐỂ KIỂM TRA)

| Thành phần | Ảnh hưởng |
|-----------|----------|
| Quỹ NV | Giảm |
| Quỹ công ty | Tăng |
| Doanh thu | ❌ Không |
| VAT | ❌ Không |
| Công nợ | ❌ Không |

---

## VII. NHỮNG ĐIỀU BỊ CẤM TUYỆT ĐỐI

- Dùng thu ngân để ghi doanh thu
- Dùng thu ngân thay cho phiếu thu
- API cập nhật quỹ trực tiếp
- API sinh VAT
- API sửa công nợ

👉 Vi phạm = phá hệ thống kế toán

---

## VIII. CHECKLIST REVIEW API THU NGÂN

- Có nhầm thu ngân với thu tiền bán không?
- Có tạo hóa đơn bán không?
- Có sinh VAT không?
- Có update quỹ trong API không?

👉 Có → **API SAI – LOẠI**

---

## IX. QUẢN TRỊ

- Thu ngân = dịch chuyển tiền
- Không được gộp với thu/chi
- File này là **KHÓA DOANH THU**
