api_ctvt3/
│
├── docs/                                   # TÀI LIỆU – NÃO BỘ HỆ THỐNG
│   │
│   ├── 01_nghiep_vu/
│   │   ├── so_do_1_nghiep_vu.md
│   │   └── mo_ta_nghiep_vu_ctvt3.md
│   │
│   ├── 02_su_kien/
│   │   └── danh_sach_su_kien_nghiep_vu.md
│   │
│   ├── 03_du_lieu/
│   │   ├── so_do_2_phan_vai_du_lieu.md
│   │   └── so_do_3_kien_truc_db.md
│   │
│   ├── 04_quy_tac/
│   │   └── quy_tac_bat_bien.md
│   │
│   ├── 05_luong_xu_ly/
│   │   └── luong_xu_ly_chuan.md
│   │
│   ├── 06_api_contract/
│   │   ├── ban_gas.md
│   │   ├── nhap_gas.md
│   │   ├── thu_chi.md
│   │   ├── thu_ngan.md
│   │   ├── ke_toan.md
│   │   └── bao_cao.md
│   │
│   ├── 07_kien_truc_code.md
│   └── 08_trien_khai_test.md
│
├── core/                                   # CORE TRANSACTION – NGUỒN SỰ THẬT (LỚP A)
│   │
│   ├── README.md
│   │
│   ├── entities/
│   │   ├── hoa_don_ban.py
│   │   ├── hoa_don_ban_chi_tiet.py
│   │   ├── hoa_don_nhap.py
│   │   ├── hoa_don_nhap_chi_tiet.py
│   │   ├── thu_chi.py
│   │   ├── thu_ngan.py
│   │   ├── hoa_don_vat.py
│   │   └── gas_du.py
│   │
│   └── repositories/
│       ├── hoa_don_ban_repo.py
│       ├── hoa_don_nhap_repo.py
│       ├── thu_chi_repo.py
│       ├── thu_ngan_repo.py
│       ├── hoa_don_vat_repo.py
│       └── gas_du_repo.py
|	│
|
    └── enums/                 # Enum dùng chung cho CORE
   	 ├── trang_thai_chung_tu.py
    	 ├── loai_thu_chi.py
    	 ├── loai_vat.py
    	 └── hinh_thuc_thanh_toan.py


│
├── journal/                                # NHẬT KÝ – HỆ QUẢ (LỚP B – KHÔNG API)
│   │
│   ├── README.md
│   │
│   ├── entities/
│   │   ├── nhat_ky_kho.py
│   │   ├── nhat_ky_vo.py
│   │   └── log_chung_tu.py
│   │
│   ├── builders/
│   │   ├── kho_from_hoa_don_nhap.py
│   │   ├── kho_from_hoa_don_ban.py
│   │   ├── vo_from_hoa_don_ban.py
│   │   └── chung_tu_from_core.py
│   │
│   ├── writers/
│   │   ├── nhat_ky_kho_writer.py
│   │   ├── nhat_ky_vo_writer.py
│   │   └── log_chung_tu_writer.py
│   │
│   └── enums/
│       ├── loai_nhat_ky_kho.py
│       ├── loai_nhat_ky_vo.py
│       └── loai_su_kien_chung_tu.py
│
├── snapshot/                               # CHỐT / BÁO CÁO – READ ONLY (LỚP C)
│   │
│   ├── README.md
│   │
│   ├── entities/
│   │   ├── ton_kho_chot_ngay.py
│   │   ├── gas_du_chot_ngay.py
│   │   ├── quy_cong_ty_chot_ngay.py
│   │   └── quy_nhan_vien_chot_ngay.py
│   │
│   ├── jobs/
│   │   ├── chot_ton_kho_ngay.py
│   │   ├── chot_gas_du_ngay.py
│   │   ├── chot_quy_cong_ty_ngay.py
│   │   └── chot_quy_nhan_vien_ngay.py
│   │
│   └── readers/
│       ├── ton_kho_reader.py
│       ├── cong_no_reader.py
│       ├── loi_nhuan_reader.py
│       └── vat_reader.py
│
├── master/                                 # DANH MỤC – KHÔNG SINH SỐ (LỚP D)
│   │
│   ├── README.md
│   │
│   ├── entities/
│   │   ├── khach_hang.py
│   │   ├── nha_cung_cap.py
│   │   ├── nhan_vien.py
│   │   ├── kho_hang.py
│   │   ├── san_pham.py
│   │   └── nhan_vien_kho.py
│   │
│   ├── repositories/
│   │   ├── khach_hang_repo.py
│   │   ├── nha_cung_cap_repo.py
│   │   ├── nhan_vien_repo.py
│   │   ├── kho_hang_repo.py
│   │   ├── san_pham_repo.py
│   │   └── nhan_vien_kho_repo.py
│   │
│   ├── services/
│   │   ├── khach_hang_service.py
│   │   ├── nha_cung_cap_service.py
│   │   ├── nhan_vien_service.py
│   │   ├── kho_hang_service.py
│   │   └── san_pham_service.py
│   │
│   ├── controllers/
│   │   ├── khach_hang_controller.py
│   │   ├── nha_cung_cap_controller.py
│   │   ├── nhan_vien_controller.py
│   │   ├── kho_hang_controller.py
│   │   └── san_pham_controller.py
│   │
│   ├── validators/
│   │   ├── khach_hang_validator.py
│   │   ├── nha_cung_cap_validator.py
│   │   ├── nhan_vien_validator.py
│   │   └── san_pham_validator.py
│   │
│   └── enums/
│       ├── trang_thai_su_dung.py
│       ├── loai_san_pham.py
│       └── vai_tro_nhan_vien.py
│
├── modules/                                # MODULE NGHIỆP VỤ – TRÁI TIM API
│   │
│   ├── README.md
│   │
│   ├── ban_gas/
│   │   ├── README.md
│   │   ├── controllers/ban_gas_controller.py
│   │   ├── services/ban_gas_service.py
│   │   ├── commands/
│   │   │   ├── tao_hoa_don_ban.py
│   │   │   ├── them_chi_tiet_ban.py
│   │   │   └── xac_nhan_hoa_don_ban.py
│   │   ├── rules/ban_gas_rules.py
│   │   └── events/hoa_don_ban_da_ghi_nhan.py
│   │
│   ├── nhap_gas/
│   │   ├── README.md
│   │   ├── controllers/nhap_gas_controller.py
│   │   ├── services/nhap_gas_service.py
│   │   ├── commands/
│   │   │   ├── tao_hoa_don_nhap.py
│   │   │   ├── them_chi_tiet_nhap.py
│   │   │   └── xac_nhan_hoa_don_nhap.py
│   │   ├── rules/nhap_gas_rules.py
│   │   └── events/hoa_don_nhap_da_ghi_nhan.py
│   │
│   ├── thu_chi/
│   │   ├── README.md
│   │   ├── controllers/thu_chi_controller.py
│   │   ├── services/thu_chi_service.py
│   │   ├── commands/
│   │   │   ├── ghi_nhan_phieu_thu.py
│   │   │   └── ghi_nhan_phieu_chi.py
│   │   ├── rules/thu_chi_rules.py
│   │   └── events/
│   │       ├── phieu_thu_da_ghi_nhan.py
│   │       └── phieu_chi_da_ghi_nhan.py
│   │
│   ├── thu_ngan/
│   │   ├── README.md
│   │   ├── controllers/thu_ngan_controller.py
│   │   ├── services/thu_ngan_service.py
│   │   ├── commands/ghi_nhan_nop_tien.py
│   │   ├── rules/thu_ngan_rules.py
│   │   └── events/nop_tien_nv_da_ghi_nhan.py
│   │
│   ├── ke_toan/
│   │   ├── README.md
│   │   ├── controllers/ke_toan_controller.py
│   │   ├── services/ke_toan_service.py
│   │   ├── commands/tao_hoa_don_vat_can_thue.py
│   │   ├── rules/ke_toan_rules.py
│   │   └── events/hoa_don_vat_can_thue_da_ghi_nhan.py
│   │
│   └── bao_cao/
│       ├── README.md
│       ├── controllers/bao_cao_controller.py
│       ├── readers/
│       │   ├── ton_kho_reader.py
│       │   ├── cong_no_reader.py
│       │   ├── loi_nhuan_reader.py
│       │   └── vat_reader.py
│       └── rules/bao_cao_rules.py
│
├── system/                                 # HỆ THỐNG – BAO NGOÀI (LỚP H)
│   │
│   ├── README.md
│   │
│   ├── auth/
│   │   ├── README.md
│   │   ├── controllers/auth_controller.py
│   │   ├── services/auth_service.py
│   │   ├── repositories/
│   │   │   ├── user_repo.py
│   │   │   └── user_session_repo.py
│   │   ├── entities/
│   │   │   ├── user.py
│   │   │   └── user_session.py
│   │   └── rules/auth_rules.py
│   │
│   ├── permission/
│   │   ├── README.md
│   │   ├── entities/
│   │   │   ├── role.py
│   │   │   ├── permission.py
│   │   │   └── role_permission.py
│   │   ├── repositories/
│   │   │   ├── role_repo.py
│   │   │   ├── permission_repo.py
│   │   │   └── role_permission_repo.py
│   │   ├── services/permission_service.py
│   │   └── enums/
│   │       ├── role_code.py
│   │       └── permission_code.py
│   │
│   ├── chat/
│   │   ├── README.md
│   │   ├── entities/
│   │   │   ├── phong_chat.py
│   │   │   ├── phong_chat_thanh_vien.py
│   │   │   └── tin_nhan.py
│   │   ├── repositories/
│   │   │   ├── phong_chat_repo.py
│   │   │   ├── phong_chat_thanh_vien_repo.py
│   │   │   └── tin_nhan_repo.py
│   │   ├── services/chat_service.py
│   │   └── controllers/chat_controller.py
│   │
│   ├── audit/
│   │   ├── README.md
│   │   ├── entities/audit_log.py
│   │   ├── repositories/audit_log_repo.py
│   │   └── writers/audit_log_writer.py
│   │
│   └── enums/
│       ├── trang_thai_user.py
│       ├── loai_log_audit.py
│       └── loai_su_kien_he_thong.py
│
├── common/                                 # DÙNG CHUNG – KỸ THUẬT (CUỐI)
│   │
│   ├── README.md
│   │
│   ├── exceptions/
│   │   ├── base_exception.py
│   │   ├── business_exception.py
│   │   ├── permission_exception.py
│   │   └── validation_exception.py
│   │
│   ├── constants/
│   │   ├── app_constants.py
│   │   ├── datetime_constants.py
│   │   └── pagination_constants.py
│   │
│   ├── enums/
│   │   ├── trang_thai_chung.py
│   │   ├── loai_tien_te.py
│   │   └── hinh_thuc_thanh_toan.py
│   │
│   ├── utils/
│   │   ├── datetime_utils.py
│   │   ├── string_utils.py
│   │   ├── number_utils.py
│   │   └── id_generator.py
│   │
│   ├── validators/
│   │   ├── base_validator.py
│   │   ├── pagination_validator.py
│   │   └── request_validator.py
│   │
│   ├── decorators/
│   │   ├── require_permission.py
│   │   ├── transactional.py
│   │   └── audit_log.py
│   │
│   └── pagination/
│       ├── page_request.py
│       └── page_response.py
│
├── config.py
├── main.py
└── README.md
