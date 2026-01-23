# JOURNAL – NHẬT KÝ HỆ QUẢ

Thư mục `journal/` dùng để ghi nhận HỆ QUẢ sau khi nghiệp vụ đã xảy ra.

Nguồn dữ liệu:
- Event phát ra từ modules
- Core entities đã chốt

Nguyên tắc bất biến:
- Journal KHÔNG chứa logic nghiệp vụ
- Journal KHÔNG kiểm tra đúng / sai
- Journal chỉ ghi lại SỰ ĐÃ XẢY RA

Cấu trúc:
- entities: mapping bảng nhật ký
- builders: dựng dòng nhật ký từ core / event
- writers: ghi dữ liệu xuống database
- enums: enum riêng cho nhật ký
