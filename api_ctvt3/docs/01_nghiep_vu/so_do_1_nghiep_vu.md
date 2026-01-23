# SƠ ĐỒ 1 – NGHIỆP VỤ HỆ THỐNG CTVT3
(BẢN CHUẨN CUỐI – KHÔNG CHỈNH)

---

## I. MỤC ĐÍCH

Tài liệu này mô tả **toàn bộ nghiệp vụ thực tế** của công ty CTVT.

Sơ đồ 1 chỉ trả lời 3 câu hỏi:
1. Công ty làm những việc gì?
2. Mỗi việc tạo ra chứng từ gì?
3. Việc đó ảnh hưởng đến đâu (kho – tiền – công nợ – VAT – lợi nhuận)?

❌ KHÔNG mô tả:
- Bảng CSDL  
- API  
- Logic kỹ thuật  

👉 Đây là **góc nhìn đời thật**, không phải góc nhìn lập trình.

---

## II. DANH SÁCH NGHIỆP VỤ GỐC

Hệ thống CTVT3 có **08 nghiệp vụ chính**, bao trùm toàn bộ vận hành:

1. Quản lý danh mục  
2. Nhập gas  
3. Bán gas  
4. Thu – chi phát sinh  
5. Thu ngân (nhân viên nộp tiền)  
6. Đặt hàng (khách / nhà cung cấp)  
7. Quản lý tổng hợp – công nợ – VAT – lợi nhuận  
8. Kế toán dịch vụ – cân thuế VAT  

👉 Ngoài 8 nghiệp vụ này, **không có nghiệp vụ kế toán nào khác**.

---

## III. CHI TIẾT TỪNG NGHIỆP VỤ

---

### (1) QUẢN LÝ DANH MỤC

**Công việc**
- Quản lý khách hàng  
- Quản lý nhà cung cấp  
- Quản lý nhân viên  
- Quản lý kho  
- Quản lý sản phẩm  
- Quản lý danh mục công nợ (chỉ khai báo, không ghi số dư)

**Tạo ra**
- Thông tin danh mục

**Ảnh hưởng**
- Không ảnh hưởng kho  
- Không ảnh hưởng quỹ  
- Không phát sinh công nợ  

👉 Đây là **nghiệp vụ nền**, không sinh số liệu.

---

### (2) NHẬP GAS

**Công việc**
- Nhập gas từ nhà cung cấp

**Tạo ra**
- Hóa đơn nhập

**Ảnh hưởng**
- Tăng tồn kho gas  
- Phát sinh công nợ nhà cung cấp (tiền)  
- Phát sinh công nợ vỏ nhà cung cấp (nếu có)  
- Giảm quỹ công ty (nếu thanh toán ngay)  
- Giảm quỹ nhân viên (nếu nhân viên ứng tiền)  
- Nếu thanh toán chuyển khoản:
  - Phát sinh VAT đầu vào  
  - VAT được cộng vào giá trị tồn kho  
- Giảm gas dư (nếu có gas dư trả nhà cung cấp)

---

### (3) BÁN GAS (NGHIỆP VỤ TRUNG TÂM)

**Công việc**
- Bán gas cho khách hàng

**Tạo ra**
- Hóa đơn bán

**Ảnh hưởng**
- Giảm tồn kho gas  
- Phát sinh tiền khách trả:
  - Tiền mặt → quỹ nhân viên  
  - Chuyển khoản → quỹ công ty  
- Phát sinh VAT đầu ra (nếu có)  
- Phát sinh công nợ khách hàng (nếu bán thiếu)  
- Phát sinh công nợ vỏ khách  
- Phát sinh gas dư (bán theo kg)

**Ghi chú**
- Một hóa đơn bán có thể đồng thời ảnh hưởng:
  - kho  
  - tiền  
  - công nợ  
  - vỏ  
  - gas dư  
  - VAT  

👉 Đây là **nghiệp vụ sinh số nhiều nhất**.

---

### (4) THU – CHI PHÁT SINH

**Công việc**
- Thu – chi ngoài hóa đơn bán / nhập  
  (xăng xe, chi phí lặt vặt, ứng trước…)

**Tạo ra**
- Phiếu thu  
- Phiếu chi  

**Ảnh hưởng**
- Quỹ nhân viên (thường là tiền mặt)  
- Quỹ công ty  
- Công nợ khách / nhà cung cấp (nếu liên quan)  
- Có thể phát sinh VAT đầu vào  

---

### (5) THU NGÂN (NHÂN VIÊN NỘP TIỀN)

**Công việc**
- Nhân viên bán hàng nộp tiền về công ty

**Tạo ra**
- Phiếu nộp tiền

**Ảnh hưởng**
- Giảm quỹ nhân viên  
- Tăng quỹ công ty  

**Ghi chú**
- Không tạo doanh thu  
- Chỉ là **dịch chuyển tiền**

---

### (6) ĐẶT HÀNG

#### (6.1) Khách đặt hàng trước (bán trước – thu tiền sau)

**Tạo ra**
- Phiếu thu

**Ảnh hưởng**
- Công nợ khách hàng (âm)  
- Quỹ nhân viên / quỹ công ty (nếu có thu tiền)  
- Có thể phát sinh VAT đầu ra  

---

#### (6.2) Đặt hàng nhà cung cấp (mua trước – trả tiền sau)

**Tạo ra**
- Phiếu chi

**Ảnh hưởng**
- Công nợ nhà cung cấp (dương)  
- Quỹ công ty (nếu có chi tiền)  
- Có thể phát sinh VAT đầu vào  

---

### (7) QUẢN LÝ TỔNG HỢP – CÔNG NỢ – VAT – LỢI NHUẬN

**Công việc**
- Quản lý hóa đơn VAT (đầu vào / đầu ra)  
- Quản lý công nợ khách hàng (tiền + vỏ)  
- Quản lý công nợ nhà cung cấp (tiền + vỏ)  
- Theo dõi, đối soát số liệu  
- Đối soát tồn kho theo kỳ  
- Quản lý lợi nhuận nhân viên theo ngày, tháng  

**Tạo ra**
- Hóa đơn VAT  
- Số dư công nợ  
- Báo cáo đối soát  
- Báo cáo lợi nhuận  

**Ảnh hưởng**
- Không ảnh hưởng trực tiếp kho  
- Không ảnh hưởng trực tiếp quỹ  
- Chỉ tổng hợp từ dữ liệu đã phát sinh hợp lệ  

---

### (8) KẾ TOÁN DỊCH VỤ – CÂN THUẾ VAT

**Bản chất**
- Xuất hóa đơn VAT **không gắn với giao dịch bán thực tế**
- Mục đích: cân đối thuế

**Công việc**
- Lập hóa đơn VAT không tên / khách lẻ  
- Theo dõi VAT cân thuế để báo cáo  

**Tạo ra**
- Hóa đơn VAT cân thuế  

**Ảnh hưởng**
- Không ảnh hưởng kho  
- Không ảnh hưởng công nợ khách  
- Phát sinh VAT đầu ra phải nộp  

**Ghi chú**
- Không tính vào doanh thu bán hàng  
- Không tính vào lợi nhuận nhân viên  

---

## IV. TRẠNG THÁI CHỨNG TỪ (ÁP DỤNG TOÀN HỆ THỐNG)

Áp dụng cho:
- Hóa đơn nhập  
- Hóa đơn bán  
- Phiếu thu  
- Phiếu chi  
- Phiếu nộp tiền  
- Hóa đơn VAT (kể cả VAT cân thuế)

**Các trạng thái**
1. Nháp  
2. Đã ghi nhận  
3. Hủy  

**Nguyên tắc**
- Chỉ chứng từ ở trạng thái **Đã ghi nhận**
  mới được dùng để tính:
  - kho  
  - quỹ  
  - công nợ  
  - VAT  
  - lợi nhuận  

---

## V. NGUYÊN TẮC KHÓA CUỐI (BẤT DI BẤT DỊCH)

1. Mọi giao dịch đều bắt nguồn từ nghiệp vụ  
2. Mọi nghiệp vụ đều tạo ra chứng từ  
3. Mỗi chứng từ bắt buộc có trạng thái  
4. Chỉ chứng từ hợp lệ mới ảnh hưởng số liệu  
5. Không bảng hoặc API nào tự ý thay đổi số dư  
6. Báo cáo chỉ là tổng hợp dữ liệu hợp lệ  
7. Hóa đơn VAT có thể tồn tại độc lập với bán hàng,
   nhưng vẫn phải tổng hợp để báo cáo thuế  

---

## VI. GHI CHÚ QUẢN TRỊ

- File này là **chuẩn nghiệp vụ gốc**  
- Mọi thiết kế DB, API, CODE **bắt buộc tuân theo**
- Chỉ ADMIN (Sếp) được phép quyết định thay đổi

---
