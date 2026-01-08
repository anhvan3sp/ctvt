-- =====================================================
-- 001_init.sql
-- Khoi tao CSDL du an CTVT
-- Tao bang, khoa, trigger, view (KHONG DU LIEU)
-- =====================================================

-- =========================
-- DATABASE
-- =========================
CREATE DATABASE IF NOT EXISTS ct_vt
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE ct_vt;

-- =========================
-- DANH MUC CO BAN
-- =========================
CREATE TABLE khach_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kh VARCHAR(50) UNIQUE,
    ten_kh VARCHAR(255),
    ten_khach_bi_danh VARCHAR(100),
    dia_chi VARCHAR(255),
    sdt VARCHAR(20),
    mst VARCHAR(20)
);

CREATE TABLE nha_cung_cap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_ncc VARCHAR(50) UNIQUE,
    ten_ncc VARCHAR(255),
    dia_chi VARCHAR(255),
    sdt VARCHAR(20),
    mst VARCHAR(20)
);

CREATE TABLE nhan_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_nv VARCHAR(50) UNIQUE,
    ten_nv VARCHAR(255),
    sdt VARCHAR(20),
    vai_tro ENUM('admin','ban_hang','ke_toan','ke_toan_online'),
    trang_thai VARCHAR(20)
);

CREATE TABLE kho_hang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kho VARCHAR(20) UNIQUE,
    ten_kho VARCHAR(255)
);

CREATE TABLE san_pham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_sp VARCHAR(50) UNIQUE,
    ten_sp VARCHAR(255),
    loai_sp ENUM('gas_binh','gas_le','gas_mini') DEFAULT 'gas_binh',
    dung_tich_kg DECIMAL(6,2)
);

-- =========================
-- HOA DON - DON HANG
-- =========================
CREATE TABLE hoa_don_ban (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    so_hd VARCHAR(50),
    ma_kh VARCHAR(50),
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    ma_nv VARCHAR(50),
    so_luong DECIMAL(10,2),
    gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2) GENERATED ALWAYS AS (so_luong * gia) STORED,
    vat_rate DECIMAL(5,2) DEFAULT 8.00,
    tien_mat DECIMAL(18,2),
    tien_ck DECIMAL(18,2),
    no_lai DECIMAL(18,2),
    ghi_chu TEXT,
    doi_vo TINYINT(1) DEFAULT 0,
    so_vo_giao INT DEFAULT 0,
    so_vo_thu INT DEFAULT 0,
    vat_amount DECIMAL(18,2) GENERATED ALWAYS AS (thanh_tien * vat_rate / 100) STORED,
    tong_tien_sau_thue DECIMAL(18,2) GENERATED ALWAYS AS (thanh_tien + vat_amount) STORED,

    FOREIGN KEY (ma_kh) REFERENCES khach_hang(ma_kh),
    FOREIGN KEY (ma_sp) REFERENCES san_pham(ma_sp),
    FOREIGN KEY (ma_kho) REFERENCES kho_hang(ma_kho),
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);

CREATE TABLE hoa_don_nhap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    ma_ncc VARCHAR(50),
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    ma_nv VARCHAR(50),
    so_luong DECIMAL(10,2),
    gia DECIMAL(18,2),
    thanh_tien DECIMAL(18,2) GENERATED ALWAYS AS (so_luong * gia) STORED,
    vat_rate DECIMAL(5,2) DEFAULT 8.00,
    tien_mat DECIMAL(18,2),
    tien_ck DECIMAL(18,2),
    no_lai DECIMAL(18,2),
    ghi_chu TEXT,

    FOREIGN KEY (ma_ncc) REFERENCES nha_cung_cap(ma_ncc),
    FOREIGN KEY (ma_sp) REFERENCES san_pham(ma_sp),
    FOREIGN KEY (ma_kho) REFERENCES kho_hang(ma_kho),
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);

-- =========================
-- CONG NO - TON KHO
-- =========================
CREATE TABLE cong_no_khach (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_kh VARCHAR(50),
    no_tien DECIMAL(18,2),
    no_vo INT,
    ngay_cap_nhat DATETIME,
    FOREIGN KEY (ma_kh) REFERENCES khach_hang(ma_kh)
);

CREATE TABLE cong_no_ncc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_ncc VARCHAR(50),
    no_tien DECIMAL(18,2),
    no_vo INT,
    ngay_cap_nhat DATETIME,
    FOREIGN KEY (ma_ncc) REFERENCES nha_cung_cap(ma_ncc)
);

CREATE TABLE ton_kho_thuc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sp_id INT,
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    ton_kho DECIMAL(10,2),
    FOREIGN KEY (sp_id) REFERENCES san_pham(id),
    FOREIGN KEY (ma_kho) REFERENCES kho_hang(ma_kho)
);

-- =========================
-- NHAT KY
-- =========================
CREATE TABLE nhat_ky_kho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    ma_sp VARCHAR(50),
    ma_kho VARCHAR(20),
    so_luong DECIMAL(10,2),
    loai_gd ENUM('nhap','ban','kiem_ke'),
    id_tham_chieu INT,
    ghi_chu VARCHAR(255)
);

CREATE TABLE nhat_ky_vo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    ma_kh VARCHAR(50),
    loai_vo ENUM('12kg','45kg','mini'),
    loai_giao_dich ENUM('giao','thu','doi'),
    so_luong INT,
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    ghi_chu TEXT,
    FOREIGN KEY (ma_kh) REFERENCES khach_hang(ma_kh)
);

-- =========================
-- TAI CHINH
-- =========================
CREATE TABLE thu_chi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay DATE,
    ma_nv VARCHAR(50),
    so_tien DECIMAL(18,2),
    hinh_thuc ENUM('tien_mat','chuyen_khoan'),
    loai_gd ENUM('thu','chi'),
    danh_muc VARCHAR(100),
    noi_dung VARCHAR(255),
    bang_tham_chieu VARCHAR(50),
    id_tham_chieu INT,
    FOREIGN KEY (ma_nv) REFERENCES nhan_vien(ma_nv)
);

CREATE TABLE thu_ngan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay_nop DATE,
    nhan_vien VARCHAR(100),
    tien_mat DECIMAL(18,2),
    tong_tien_ck DECIMAL(18,2),
    ghi_chu VARCHAR(255)
);

-- =========================
-- GHI CHU
-- =========================
-- File nay KHONG chua du lieu
-- Du lieu mau / du lieu that de o file khac (seed)
-- Moi thay doi schema tao file 002_*.sql tro di
