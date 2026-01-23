# QUY TẮC BẤT BIẾN – HỆ THỐNG CTVT3
(BẢN CHUẨN CUỐI – KHÔNG ĐƯỢC PHÁ)

---

## I. MỤC ĐÍCH

Tài liệu này tập hợp **TOÀN BỘ CÁC QUY TẮC BẤT BIẾN**  
đã được chốt trong dự án CTVT3, nhằm:

1. Ngăn hệ thống bị biến dạng khi code
2. Làm chuẩn để review:
   - DB
   - API
   - logic xử lý
3. Là “luật tối cao” khi có tranh luận kỹ thuật

👉 **Vi phạm 1 quy tắc = hệ thống sai bản chất.**

---

## II. QUY TẮC NGUỒN SỰ THẬT (CORE)

1. Mọi con số **chỉ được sinh ra từ CORE_GIAO_DICH**
2. Không bảng nào khác được coi là nguồn sự thật
3. CORE:
   - ghi sự kiện
   - không ghi kết quả tổng hợp
4. Không tính ngược CORE từ:
   - nhật ký
   - snapshot
   - báo cáo

👉 **Sai CORE = sai toàn bộ hệ thống**

---

## III. QUY TẮC CHỨNG TỪ

5. Mọi nghiệp vụ **bắt buộc phải có chứng từ**
6. Mỗi chứng từ **bắt buộc có trạng thái**
7. Chỉ chứng từ ở trạng thái:
   - **ĐÃ GHI NHẬN**
   mới được phép sinh số
8. Không được sửa số trên chứng từ đã ghi nhận  
   → nếu sai, tạo **chứng từ điều chỉnh mới**

---

## IV. QUY TẮC SINH SỐ

9. Không có sự kiện → không được sinh số
10. Mỗi API nghiệp vụ phải đại diện cho **1 sự kiện**
11. Sinh số **chỉ xảy ra tại thời điểm ghi nhận**
12. Cấm tuyệt đối:
    - update tồn kho
    - update công nợ
    - update quỹ
    bằng tay hoặc API riêng

---

## V. QUY TẮC NHẬT KÝ & SNAPSHOT

13. Nhật ký:
    - chỉ ghi hệ quả
    - không được dùng để tính số
14. Snapshot:
    - chỉ là ảnh chụp
    - có thể xóa và build lại
    - không bao giờ là nguồn sự thật
15. Báo cáo:
    - chỉ đọc
    - không được ghi DB

---

## VI. QUY TẮC VAT

16. VAT **tách khỏi doanh thu**
17. VAT sinh tự động khi:
    - nhập hàng chuyển khoản
    - bán hàng chuyển khoản
18. VAT cân thuế:
    - không gắn bán hàng
    - không tính doanh thu
    - không tính lợi nhuận
19. Mọi VAT đều phải tổng hợp để báo cáo thuế

---

## VII. QUY TẮC QUỸ & CÔNG NỢ

20. Quỹ gồm:
    - quỹ công ty
    - quỹ nhân viên
21. Quỹ chỉ thay đổi thông qua:
    - phiếu thu
    - phiếu chi
    - phiếu thu ngân
22. Công nợ:
    - không lưu số dư tĩnh
    - luôn tính từ giao dịch
23. Công nợ có thể:
    - dương
    - âm
    tùy nghiệp vụ

---

## VIII. QUY TẮC PHÂN QUYỀN

24. Quyền gắn với **VAI TRÒ**, không gắn người
25. Nhân viên:
    - không được tự chốt số
26. Chuyển khoản:
    - bắt buộc qua kế toán
27. Không ai được:
    - sửa số liệu đã chốt
    - can thiệp snapshot

---

## IX. QUY TẮC THIẾT KẾ API

28. API không tính toán kế toán
29. API không ghi snapshot
30. API không ghi nhật ký bằng tay
31. API không tồn tại nếu:
    - không đại diện cho sự kiện
32. Điều chỉnh sai → tạo API cho **sự kiện mới**

---

## X. CHECKLIST KIỂM TRA NHANH

Khi xem bất kỳ DB / API / CODE, chỉ cần hỏi:

- Có vi phạm nguồn sự thật không?
- Có sinh số ngoài CORE không?
- Có update số trực tiếp không?
- Có tính ngược không?

👉 Có **1 câu trả lời “CÓ”** → **SAI THIẾT KẾ**.

---

## XI. QUẢN TRỊ TÀI LIỆU

- File này là **LUẬT BẤT BIẾN**
- Chỉ ADMIN (Sếp) được quyền sửa
- Sửa file này = đổi bản chất hệ thống
- Mọi thay đổi phải ghi:
  - ngày
  - lý do
  - phạm vi ảnh hưởng

---
