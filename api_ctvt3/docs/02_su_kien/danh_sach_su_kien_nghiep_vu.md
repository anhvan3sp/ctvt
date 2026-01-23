# SƠ ĐỒ 2A – DANH SÁCH SỰ KIỆN NGHIỆP VỤ CTVT3
(BẢN CHUẨN CUỐI – KHÓA SINH SỐ)

---

## I. MỤC ĐÍCH

Tài liệu này xác định **TOÀN BỘ CÁC SỰ KIỆN NGHIỆP VỤ**  
là **NGUỒN DUY NHẤT** được phép làm thay đổi số liệu trong hệ thống CTVT3.

Sơ đồ 2A dùng để:
1. Xác định **thời điểm hệ thống được phép sinh số**
2. Ràng buộc **API chỉ được đại diện cho sự kiện**
3. Cấm tuyệt đối các hành vi:
   - update số cho tiện
   - tính ngược từ báo cáo
   - sửa số ngoài chứng từ

👉 **Không có sự kiện → không được sinh số.**

---

## II. ĐỊNH NGHĨA “SỰ KIỆN NGHIỆP VỤ”

**Sự kiện nghiệp vụ** là:
- Một hành động thực tế xảy ra trong công ty
- BẮT BUỘC gắn với một chứng từ
- Có thời điểm ghi nhận rõ ràng
- Có thể ảnh hưởng đến:
  - kho
  - tiền
  - công nợ
  - VAT
  - lợi nhuận

❌ KHÔNG PHẢI sự kiện nghiệp vụ:
- sửa ghi chú
- xem báo cáo
- CRUD danh mục
- thao tác hệ thống (login, chat, log)

---

## III. PHÂN LOẠI SỰ KIỆN

CTVT3 chia sự kiện thành **3 nhóm duy nhất**:

1. **SỰ KIỆN SINH SỐ (CORE EVENT)**  
2. **SỰ KIỆN THAY ĐỔI TRẠNG THÁI (KHÔNG SINH SỐ)**  
3. **HÀNH VI KHÔNG PHẢI NGHIỆP VỤ**

👉 Chỉ **nhóm (1)** được phép làm thay đổi số liệu.

---

## IV. DANH SÁCH SỰ KIỆN SINH SỐ (CORE EVENT)

> Chỉ các sự kiện trong mục này  
> mới được phép sinh số – ghi CORE – sinh hệ quả.

---

### (E1) XÁC NHẬN HÓA ĐƠN NHẬP GAS

- Nghiệp vụ: Nhập gas
- Chứng từ: Hóa đơn nhập
- Thời điểm sinh số: khi **chuyển sang trạng thái ĐÃ GHI NHẬN**

**Ảnh hưởng**
- Tăng tồn kho gas
- Phát sinh công nợ nhà cung cấp
- Giảm quỹ (nếu thanh toán)
- Phát sinh VAT đầu vào (nếu chuyển khoản)

---

### (E2) XÁC NHẬN HÓA ĐƠN BÁN GAS

- Nghiệp vụ: Bán gas
- Chứng từ: Hóa đơn bán
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN**

**Ảnh hưởng**
- Giảm tồn kho
- Tăng tiền (quỹ NV hoặc quỹ công ty)
- Phát sinh công nợ khách (nếu bán thiếu)
- Phát sinh VAT đầu ra
- Phát sinh vỏ gas / gas dư (nếu có)

---

### (E3) GHI NHẬN PHIẾU THU

- Nghiệp vụ: Thu – chi / Đặt hàng khách
- Chứng từ: Phiếu thu
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN**

**Ảnh hưởng**
- Tăng quỹ nhân viên hoặc quỹ công ty
- Giảm công nợ khách  
  (hoặc làm công nợ âm nếu khách trả trước)
- Có thể phát sinh VAT đầu ra

---

### (E4) GHI NHẬN PHIẾU CHI

- Nghiệp vụ: Thu – chi / Đặt hàng nhà cung cấp
- Chứng từ: Phiếu chi
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN**

**Ảnh hưởng**
- Giảm quỹ
- Tăng công nợ nhà cung cấp
- Có thể phát sinh VAT đầu vào

---

### (E5) GHI NHẬN PHIẾU THU NGÂN (NHÂN VIÊN NỘP TIỀN)

- Nghiệp vụ: Thu ngân
- Chứng từ: Phiếu nộp tiền
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN**

**Ảnh hưởng**
- Giảm quỹ nhân viên
- Tăng quỹ công ty

❗ Không sinh doanh thu  
❗ Không liên quan VAT

---

### (E6) GHI NHẬN HÓA ĐƠN VAT (BÁN / NHẬP)

- Nghiệp vụ: Tổng hợp / Kế toán
- Chứng từ: Hóa đơn VAT
- Thời điểm sinh số: khi **ĐÃ GHI NHẬN THUẾ**

**Ảnh hưởng**
- Phát sinh VAT đầu vào / đầu ra
- Không ảnh hưởng kho trực tiếp

---

### (E7) GHI NHẬN HÓA ĐƠN VAT CÂN THUẾ

- Nghiệp vụ: Kế toán dịch vụ
- Chứng từ: Hóa đơn VAT cân thuế

**Ảnh hưởng**
- Phát sinh VAT phải nộp
- Không ảnh hưởng kho
- Không ảnh hưởng công nợ khách
- Không ảnh hưởng lợi nhuận nhân viên

---

## V. SỰ KIỆN THAY ĐỔI TRẠNG THÁI (KHÔNG SINH SỐ)

Các hành động sau **KHÔNG ĐƯỢC PHÉP sinh số**:

- Chuyển chứng từ về NHÁP
- Hủy chứng từ
- Sửa ghi chú
- Đính kèm file / ảnh
- Phân công nhân viên xử lý

👉 Nếu **không nằm trong Mục IV**  
→ **CẤM sinh số**.

---

## VI. HÀNH VI KHÔNG PHẢI NGHIỆP VỤ

Các hành động sau:
- CRUD danh mục
- Xem báo cáo
- Chốt snapshot
- Rebuild snapshot
- Login / chat / audit log

👉 **TUYỆT ĐỐI KHÔNG ĐƯỢC GHI CORE**

---

## VII. QUY TẮC KIỂM SOÁT API THEO SỰ KIỆN

1. Mỗi API phải đại diện cho **1 sự kiện nghiệp vụ**
2. API không gắn được với sự kiện → API SAI
3. Không tồn tại API:
   - cập nhật tồn kho
   - cập nhật công nợ
   - cập nhật quỹ
4. Điều chỉnh số liệu → **tạo sự kiện mới**

---

## VIII. CHECKLIST REVIEW (BẮT BUỘC)

Khi xem một API, phải trả lời được:
- API này đại diện cho sự kiện nào?
- Sự kiện đó có nằm trong Mục IV không?
- Sinh số ở thời điểm nào?
- Ghi vào bảng CORE nào?

👉 Không trả lời được → **CẤM VIẾT API**

---

## IX. QUẢN TRỊ TÀI LIỆU

- Đây là **FILE KHÓA SINH SỐ**
- Mọi thay đổi phải do ADMIN quyết định
- Sửa file này = sửa toàn bộ logic hệ thống

---
