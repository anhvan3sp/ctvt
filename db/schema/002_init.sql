-- ========================================
-- DB: CTVT2
-- Muc dich: Nen mong du lieu cho phan mem ban gas
-- Nguyen tac:
--  - DB KHONG lam nghiep vu
--  - KHONG trigger nghiep vu
--  - KHONG view
--  - API se xu ly toan bo logic
-- ========================================

DROP DATABASE IF EXISTS ctvt2;
CREATE DATABASE ctvt2
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE ctvt2;

-- ========================================
-- 1. DANH MUC CO DINH
-- ========================================

-- Khach hang
CREATE TABLE khach_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kh VARCHAR(50) UNIQUE,
    ten_cua_hang VARCHAR(255),
    ten_goi_khac VARCHAR(100),
    dia_chi VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    ma_so_thue VARCHAR(50),
    ghi_chu VARCHAR(255)
);

-- Nha cung cap
CREATE TABLE nha_cung_cap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_ncc VARCHAR(50) UNIQUE,
    ten_ncc VARCHAR(255),
    dia_chi VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    ma_so_thue VARCHAR(50),
    ghi_chu VARCHAR(255)
);

-- Nhan vien
CREATE TABLE nhan_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_nv VARCHAR(50) UNIQUE,
    ten_nv VARCHAR(255),
    so_dien_thoai VARCHAR(20),
    vai_tro ENUM('ban_hang','ke_toan','ke_toan_online','dac_biet'),
    trang_thai VARCHAR(20),
    ghi_chu VARCHAR(255)
);

-- Kho hang
CREATE TABLE kho_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kho VARCHAR(20) UNIQUE,
    ten_kho VARCHAR(255)
);

-- San pham
CREATE TABLE san_pham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_sp VARCHAR(50) UNIQUE,
    ten_sp VARCHAR(255),
    loai_san_pham ENUM('gas_binh','gas_mini','gas_kg','hang_hoa_khac'),
    don_vi_tinh ENUM('binh','lon','kg','cai'),
    dung_tich_kg DECIMAL(6,2) COMMENT 'Chi ap dung cho san pham gas'
);

-- ========================================
-- 2. QUY & TIEN
-- ========================================

-- Quy nhan vien (tien mat nhan vien dang cam)
CREATE TABLE quy_nhan_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_nv VARCHAR(50),
    so_du DECIMAL(18,2) DEFAULT 0,
    ngay_cap_nhat DATETIME
);

-- Quy cong ty (tong tien mat + tien ngan hang)
CREATE TABLE quy_cong_ty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tien_mat DECIMAL(18,2) DEFAULT 0,
    tien_ngan_hang DECIMAL(18,2) DEFAULT 0,
    ngay_cap_nhat DATETIME
);

-- ========================================
-- 3. HOA DON BAN
-- ========================================

CREATE TABLE hoa_don_ban (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    so_hd VARCHAR(50),
    ma_kh VARCHAR(50),
    ma_nv VARCHAR(50),
    ma_kho VARCHAR(20),
    tong_tien DECIMAL(18,2),
    tien_mat DECIMAL(18,2),
    tien_chuyen_khoan DECIMAL(18,2),
    tien_khach_tra_thua DECIMAL(18,2),
    tien_khach_thieu DECIMAL(18,2),
    ghi_chu VARCHAR(255)
);

-- Chi tiet hoa don ban
CREATE TABLE hoa_don_ban_chi_tiet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_hoa_don INT,
    ma_sp VARCHAR(50),
    so_luong DECIMAL(10,2),
    don_gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2)
);

-- ========================================
-- 4. HOA DON NHAP
-- ========================================

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
    ghi_chu VARCHAR(255)
);

CREATE TABLE hoa_don_nhap_chi_tiet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_hoa_don INT,
    ma_sp VARCHAR(50),
    so_luong DECIMAL(10,2),
    don_gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2)
);

-- ========================================
-- 5. VAT
-- ========================================

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
    id_tham_chieu INT
);

-- ========================================
-- 6. NHAT KY
-- ========================================

-- Nhat ky kho
CREATE TABLE nhat_ky_kho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATETIME,
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    so_luong DECIMAL(10,2),
    loai_giao_dich ENUM('nhap','xuat','kiem_ke'),
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    ghi_chu VARCHAR(255)
);

-- Nhat ky vo
CREATE TABLE nhat_ky_vo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATETIME,
    ma_kh VARCHAR(50),
    loai_vo ENUM('12kg','45kg','mini'),
    loai_giao_dich ENUM('giao','thu','doi'),
    so_luong INT,
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    ghi_chu VARCHAR(255)
);

-- ========================================
-- 7. THU - CHI (CHI DE GHI NHAN)
-- ========================================

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
    id_tham_chieu INT
);

-- ========================================
-- 8. THU NGAN (NOP TIEN)
-- ========================================

CREATE TABLE thu_ngan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay_nop DATE,
    ma_nv VARCHAR(50),
    tien_mat DECIMAL(18,2) DEFAULT 0,
    tien_chuyen_khoan DECIMAL(18,2) DEFAULT 0,
    ghi_chu VARCHAR(255)
);

-- ========================================
-- 9. PHONG CHAT NOI BO
-- ========================================

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
    ngay_tham_gia DATETIME DEFAULT CURRENT_TIMESTAMP
);
