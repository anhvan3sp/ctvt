-- =========================================================
-- CTVT2 - FULL INIT DATABASE
-- Version : 2.0 (CHOT)
-- Muc dich: Khoi tao CSDL cho phan mem ban gas
-- Nguyen tac:
--   - DB KHONG xu ly nghiep vu
--   - KHONG trigger nghiep vu
--   - API xu ly toan bo logic
--   - Day du nghiep vu tu 001 + 002
-- =========================================================

SET NAMES utf8mb4;
SET time_zone = '+07:00';

DROP DATABASE IF EXISTS ctvt2;
CREATE DATABASE ctvt2
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE ctvt2;

-- =========================================================
-- I. DANH MUC CO BAN
-- =========================================================

CREATE TABLE khach_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kh VARCHAR(50) UNIQUE,
    ten_cua_hang VARCHAR(255),
    ten_goi_khac VARCHAR(100),
    dia_chi VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    ma_so_thue VARCHAR(50),
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT
);

CREATE TABLE nha_cung_cap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_ncc VARCHAR(50) UNIQUE,
    ten_ncc VARCHAR(255),
    dia_chi VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    ma_so_thue VARCHAR(50),
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT
);

CREATE TABLE nhan_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_nv VARCHAR(50) UNIQUE,
    ten_nv VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    vai_tro ENUM('ban_hang','ke_toan','ke_toan_online','dac_biet'),
    trang_thai VARCHAR(20),
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT
);

CREATE TABLE kho_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kho VARCHAR(20) UNIQUE,
    ten_kho VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT
);

CREATE TABLE san_pham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_sp VARCHAR(50) UNIQUE,
    ten_sp VARCHAR(255),
    loai_san_pham ENUM('gas_binh','gas_mini','gas_kg','hang_hoa_khac'),
    don_vi_tinh ENUM('binh','lon','kg','cai'),
    dung_tich_kg DECIMAL(6,2),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT
);

-- =========================================================
-- II. QUY - TIEN
-- =========================================================

CREATE TABLE quy_nhan_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_nv VARCHAR(50),
    so_du DECIMAL(18,2) DEFAULT 0,
    ngay_cap_nhat DATETIME,

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);

CREATE TABLE quy_cong_ty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tien_mat DECIMAL(18,2) DEFAULT 0,
    tien_ngan_hang DECIMAL(18,2) DEFAULT 0,
    ngay_cap_nhat DATETIME,

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT
);

-- =========================================================
-- III. HOA DON BAN (HEADER)
-- =========================================================

CREATE TABLE hoa_don_ban (
    id INT AUTO_INCREMENT PRIMARY KEY,
    so_hd VARCHAR(50),
    ngay DATE,
    ma_kh VARCHAR(50),
    ma_nv VARCHAR(50),
    ma_kho VARCHAR(20),

    tong_tien_hang DECIMAL(18,2),
    tien_mat DECIMAL(18,2),
    tien_chuyen_khoan DECIMAL(18,2),
    tong_thanh_toan DECIMAL(18,2),
    no_lai DECIMAL(18,2),
    ghi_chu_chung VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (ma_kh) REFERENCES khach_hang(ma_kh),
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv),
    FOREIGN KEY (ma_kho) REFERENCES kho_hang(ma_kho)
);

-- =========================================================
-- IV. HOA DON BAN CHI TIET (DETAIL)
-- =========================================================

CREATE TABLE hoa_don_ban_chi_tiet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_hoa_don INT,
    stt INT,

    loai_dong ENUM(
        'ban_gas',
        'giao_vo',
        'thu_vo',
        'no_vo',
        'cuoc_van_chuyen',
        'cuoc_vo',
        'tra_no_cu'
    ),

    ma_sp VARCHAR(50),
    ten_hien_thi VARCHAR(255),
    so_luong DECIMAL(10,2),
    don_gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2),

    loai_vo ENUM('12kg','45kg','mini'),
    ghi_chu_dong VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (id_hoa_don) REFERENCES hoa_don_ban(id),
    FOREIGN KEY (ma_sp) REFERENCES san_pham(ma_sp)
);

-- =========================================================
-- V. HOA DON NHAP
-- =========================================================

CREATE TABLE hoa_don_nhap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    ma_ncc VARCHAR(50),
    ma_nv VARCHAR(50),
    ma_kho VARCHAR(20),

    tong_tien DECIMAL(18,2),
    tien_mat DECIMAL(18,2),
    tien_chuyen_khoan DECIMAL(18,2),
    tien_thanh_toan_thua DECIMAL(18,2),
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (ma_ncc) REFERENCES nha_cung_cap(ma_ncc),
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv),
    FOREIGN KEY (ma_kho) REFERENCES kho_hang(ma_kho)
);

CREATE TABLE hoa_don_nhap_chi_tiet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_hoa_don INT,
    ma_sp VARCHAR(50),
    so_luong DECIMAL(10,2),
    don_gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (id_hoa_don) REFERENCES hoa_don_nhap(id),
    FOREIGN KEY (ma_sp) REFERENCES san_pham(ma_sp)
);

-- =========================================================
-- VI. VAT
-- =========================================================

CREATE TABLE hoa_don_vat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loai ENUM('dau_vao','dau_ra'),
    so_hd_vat VARCHAR(50),
    ngay DATE,
    ten_doi_tuong VARCHAR(255),
    dia_chi VARCHAR(255),
    ma_so_thue VARCHAR(50),
    tien_truoc_thue DECIMAL(18,2),
    tien_thue DECIMAL(18,2),
    tong_tien_sau_thue DECIMAL(18,2),
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT
);

-- =========================================================
-- VII. NHAT KY
-- =========================================================

CREATE TABLE nhat_ky_kho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATETIME,
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    so_luong DECIMAL(10,2),
    loai_giao_dich ENUM('nhap','xuat','kiem_ke'),
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT
);

CREATE TABLE nhat_ky_vo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATETIME,
    ma_kh VARCHAR(50),
    loai_vo ENUM('12kg','45kg','mini'),
    loai_giao_dich ENUM('giao','thu','doi'),
    so_luong INT,
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT
);

-- =========================================================
-- VIII. THU - CHI
-- =========================================================

CREATE TABLE thu_chi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATETIME,
    doi_tuong ENUM('nhan_vien','cong_ty'),
    ma_nv VARCHAR(50),
    so_tien DECIMAL(18,2),
    hinh_thuc ENUM('tien_mat','chuyen_khoan'),
    loai_giao_dich ENUM('thu','chi'),
    noi_dung VARCHAR(255),
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
    nguoi_tao INT,
    nguoi_cap_nhat INT,

    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);

-- =========================================================
-- IX. THU NGAN (NHAN VIEN NOP TIEN MAT)
-- =========================================================

CREATE TABLE thu_ngan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay_nop DATE,
    ma_nv VARCHAR(50),
    tien_mat DECIMAL(18,2),
    ghi_chu VARCHAR(255),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao INT,

    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);
-- =========================================================
-- X. PHONG CHAT NOI BO
-- =========================================================

CREATE TABLE phong_chat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_phong VARCHAR(50) UNIQUE,
    ten_phong VARCHAR(255),
    loai_phong ENUM('nhom','rieng'),
    nguoi_tao VARCHAR(50),

    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE phong_chat_thanh_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_phong VARCHAR(50),
    ma_nv VARCHAR(50),
    vai_tro ENUM('admin','thanh_vien'),

    ngay_tham_gia DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (ma_phong) REFERENCES phong_chat(ma_phong),
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);


-- =========================================================
-- END OF FILE
-- =========================================================
