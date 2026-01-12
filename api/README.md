# CTVT2 API – Định hướng thiết kế & hoàn thiện

## 1. Mục tiêu

API CTVT2 được xây dựng **dựa trực tiếp trên CSDL ctvt2 đã chốt**, với mục tiêu:

* Phục vụ **vận hành thực tế** (nhập liệu, theo dõi bán hàng, thu chi)
* Là **backend chuẩn** để phát triển **app Android / Web** về sau
* Dễ mở rộng, dễ nâng cấp phiên bản, không phụ thuộc giao diện

Nguyên tắc xuyên suốt: **DB chỉ lưu dữ liệu – API xử lý toàn bộ nghiệp vụ**.

---

## 2. Phạm vi hệ thống

API bao phủ toàn bộ nghiệp vụ của công ty bán gas:

* Danh mục: khách hàng, nhà cung cấp, sản phẩm, kho, nhân viên
* Hóa đơn bán (header / detail, nhiều loại dòng)
* Hóa đơn nhập
* Thu – chi – quỹ
* Nhật ký kho, nhật ký vỏ
* Chat nội bộ (phục vụ quản lý)

API **không xử lý giao diện**, chỉ trả JSON.

---

## 3. Nguyên tắc thiết kế

### 3.1. Không làm nghiệp vụ trong DB

* Không trigger nghiệp vụ
* Không view tổng hợp
* Không tính tiền trong SQL

Mọi logic:

* tính tổng tiền
* cộng / trừ quỹ
* cập nhật công nợ
* kiểm soát tồn kho

→ **đều xử lý trong API**.

---

### 3.2. Bám chặt schema DB đã chốt

* Mỗi bảng DB tương ứng **1 hoặc nhiều API rõ ràng**
* Không tạo API “mơ hồ” không gắn với bảng nào
* Tên trường JSON bám sát tên cột DB (tiếng Việt không dấu)

---

## 4. Kiến trúc tổng thể API

### 4.1. Công nghệ

* FastAPI (Python)
* MySQL (ctvt2)
* JSON REST API

### 4.2. Cấu trúc thư mục chuẩn

```
ctvt_api/
├── main.py
├── requirements.txt
├── core/
│   ├── database.py      # Kết nối DB
│   ├── auth.py          # Xác thực
│   └── deps.py          # Dependency dùng chung
├── modules/
│   ├── khach_hang.py
│   ├── nha_cung_cap.py
│   ├── san_pham.py
│   ├── kho_hang.py
│   ├── nhan_vien.py
│   ├── hoa_don_ban.py
│   ├── hoa_don_nhap.py
│   ├── thu_chi.py
│   ├── quy.py
│   ├── nhat_ky.py
│   └── chat.py
└── schemas/
    ├── hoa_don.py
    ├── thu_chi.py
    └── common.py
```

---

## 5. Thiết kế API theo nghiệp vụ

### 5.1. Danh mục (CRUD)

Ví dụ:

```
GET    /khach-hang
POST   /khach-hang
PUT    /khach-hang/{id}
```

Nguyên tắc:

* CRUD đơn giản
* Không xử lý logic phức tạp

---

### 5.2. Hóa đơn bán

#### API tạo hóa đơn bán

```
POST /hoa-don-ban
```

API này thực hiện:

* Ghi 1 bản ghi vào `hoa_don_ban`
* Ghi N dòng vào `hoa_don_ban_chi_tiet`
* Phân loại dòng theo `loai_dong`
* Tính toán:

  * tổng tiền hàng
  * tiền khách trả
  * nợ lại

Tất cả xử lý **trong API**, DB chỉ lưu kết quả.

---

### 5.3. Hóa đơn nhập

Tương tự hóa đơn bán, nhưng dùng bảng:

* `hoa_don_nhap`
* `hoa_don_nhap_chi_tiet`

---

### 5.4. Thu – chi – quỹ

* `POST /thu-chi`
* `POST /thu-ngan`

API chịu trách nhiệm:

* Ghi nhận phát sinh
* Cập nhật `quy_cong_ty`, `quy_nhan_vien`
* Không cộng trừ trong DB

---

### 5.5. Nhật ký

* Nhật ký kho
* Nhật ký vỏ

API khác ghi dữ liệu vào bảng nhật ký,
API đọc **chỉ dùng để tra cứu, báo cáo**.

---

### 5.6. Chat nội bộ

Phục vụ quản lý, không ảnh hưởng nghiệp vụ bán hàng:

* Tạo phòng
* Thêm thành viên
* Ghi nhận lịch sử

---

## 6. Định hướng phát triển App

API được thiết kế để:

* Android app gọi trực tiếp
* Web app dùng chung backend
* Sau này có thể:

  * thêm phân quyền
  * thêm báo cáo
  * thêm dashboard

API **không phụ thuộc giao diện**, nên app có thể thay đổi mà không sửa DB.

---

## 7. Lộ trình hoàn thiện API

1. Hoàn thiện toàn bộ endpoint (CRUD + nghiệp vụ)
2. Gắn DB thật cho tất cả module
3. Kiểm thử bằng Swagger (/docs)
4. Dùng API nhập liệu thật
5. Sau cùng mới tối ưu hiệu năng, bảo mật

---

## 8. Nguyên tắc nâng version

* `ctvt2_full_init.sql` là **file DB gốc – không sửa**
* Mọi thay đổi DB về sau:

```
003_alter.sql
004_alter.sql
```

API sẽ được nâng version song song, không phá dữ liệu cũ.

---

## 9. Kết luận

CTVT2 API là **xương sống của toàn bộ hệ thống**.

* DB đã chốt
* API bám DB
* App bám API

Thiết kế này đảm bảo:

* Dùng được ngay
* Không phải làm lại
* Mở rộng được nhiều năm sau
