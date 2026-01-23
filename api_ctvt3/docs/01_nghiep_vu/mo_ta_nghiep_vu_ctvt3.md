# MÔ TẢ NGHIỆP VỤ VẬN HÀNH HỆ THỐNG CTVT3
(BẢN DIỄN GIẢI BẰNG CHỮ – THEO SƠ ĐỒ 1)

---

## I. MỤC ĐÍCH TÀI LIỆU

Tài liệu này mô tả **cách công ty CTVT vận hành ngoài đời thực**  
bằng ngôn ngữ dễ hiểu, **không kỹ thuật**, nhằm:

- Giúp dev / AI hiểu đúng nghiệp vụ
- Làm cầu nối giữa:
  - Sơ đồ nghiệp vụ (Sơ đồ 1)
  - Danh sách sự kiện
  - API sau này

❗ Tài liệu này:
- KHÔNG mô tả bảng DB
- KHÔNG mô tả API
- KHÔNG chứa thuật ngữ kỹ thuật

---

## II. TỔNG QUAN CÁCH CÔNG TY HOẠT ĐỘNG

Công ty CTVT kinh doanh gas theo mô hình:

- Nhập gas từ **nhà cung cấp**
- Bán gas cho **khách hàng**
- Nhân viên trực tiếp:
  - bán hàng
  - thu tiền
  - ứng tiền
- Công ty quản lý:
  - kho
  - quỹ
  - công nợ
  - thuế VAT

Mọi hoạt động đều phải:
- có **chứng từ**
- có **người chịu trách nhiệm**
- có **thời điểm ghi nhận rõ ràng**

---

## III. MÔ TẢ CHI TIẾT TỪNG NGHIỆP VỤ

---

### (1) QUẢN LÝ DANH MỤC

**Bản chất:**  
Chỉ là khai báo thông tin, **không tạo giao dịch**.

Danh mục gồm:
- Khách hàng
- Nhà cung cấp
- Nhân viên
- Kho
- Sản phẩm

👉 Việc tạo / sửa danh mục:
- Không làm thay đổi tiền
- Không làm thay đổi kho
- Không tạo công nợ

---

### (2) NHẬP GAS

**Tình huống thực tế:**
- Công ty mua gas từ nhà cung cấp
- Có thể:
  - trả tiền ngay
  - trả tiền sau
  - nhân viên ứng tiền

**Kết quả nghiệp vụ:**
- Có **hóa đơn nhập**
- Gas được đưa vào kho
- Phát sinh công nợ với nhà cung cấp
- Có thể phát sinh VAT đầu vào

👉 Nếu chưa xác nhận hóa đơn:
- Chỉ là ghi nháp
- Chưa ảnh hưởng số liệu

---

### (3) BÁN GAS (NGHIỆP VỤ TRUNG TÂM)

**Tình huống thực tế:**
- Nhân viên bán gas cho khách
- Khách có thể:
  - trả tiền mặt
  - chuyển khoản
  - nợ lại

**Đặc thù:**
- Một lần bán có thể đồng thời:
  - giảm kho
  - tăng tiền
  - phát sinh công nợ
  - phát sinh VAT
  - phát sinh vỏ / gas dư

👉 Đây là nghiệp vụ phức tạp nhất và là **trung tâm của hệ thống**.

---

### (4) THU – CHI PHÁT SINH

**Bản chất:**
- Các khoản tiền **không gắn trực tiếp với mua bán gas**

Ví dụ:
- Đổ xăng
- Chi phí lặt vặt
- Ứng tiền
- Thu hộ / chi hộ

👉 Vẫn phải có:
- phiếu thu
- phiếu chi
- người chịu trách nhiệm

---

### (5) THU NGÂN – NHÂN VIÊN NỘP TIỀN

**Tình huống thực tế:**
- Nhân viên bán hàng giữ tiền mặt
- Cuối ngày / cuối ca nộp về công ty

**Bản chất:**
- Chỉ là **chuyển tiền nội bộ**
- Không tạo doanh thu
- Không liên quan VAT

---

### (6) ĐẶT HÀNG

#### (6.1) Khách đặt trước

- Khách đưa tiền trước
- Chưa giao gas
- Công ty ghi nhận là **khách trả trước**

👉 Bản chất:  
**Công nợ khách có thể âm**

---

#### (6.2) Đặt hàng nhà cung cấp

- Công ty đặt gas
- Chưa nhận hàng
- Có thể trả tiền trước hoặc sau

👉 Bản chất:  
**Công nợ nhà cung cấp có thể dương**

---

### (7) QUẢN LÝ TỔNG HỢP – ĐỐI SOÁT

**Mục tiêu:**
- Biết chính xác:
  - kho còn bao nhiêu
  - ai đang nợ ai
  - lãi lỗ thế nào
  - VAT phải nộp bao nhiêu

👉 Phần này:
- Không tạo giao dịch mới
- Chỉ tổng hợp từ dữ liệu đã có

---

### (8) KẾ TOÁN DỊCH VỤ – CÂN THUẾ VAT

**Bản chất:**
- Xuất hóa đơn VAT để cân thuế
- Không gắn với bán gas thực tế

👉 Hóa đơn này:
- Không tính doanh thu
- Không tính lợi nhuận
- Chỉ phục vụ nghĩa vụ thuế

---

## IV. KẾT LUẬN NGHIỆP VỤ

1. Công ty vận hành bằng **chứng từ**
2. Chứng từ có **trạng thái**
3. Chỉ chứng từ hợp lệ mới ảnh hưởng số liệu
4. Không có khái niệm “sửa số cho khớp”
5. Sai → tạo chứng từ điều chỉnh mới

---

## V. VAI TRÒ TÀI LIỆU NÀY TRONG DỰ ÁN

- Là nền cho:
  - danh sách sự kiện
  - API contract
- Là tài liệu đọc **trước khi viết bất kỳ dòng code nào**
- Là thứ để sếp hỏi:
  > “Hệ thống này có giống công ty mình không?”

---
