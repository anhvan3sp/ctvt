-- --------------------------------------------------------
-- Host:                         192.168.1.119
-- Server version:               8.0.44-0ubuntu0.22.04.2 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             12.14.0.7165
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for ctvt3
CREATE DATABASE IF NOT EXISTS `ctvt3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ctvt3`;

-- Dumping structure for event ctvt3.ev_chot_quy_cong_ty_ngay
DELIMITER //
CREATE EVENT `ev_chot_quy_cong_ty_ngay` ON SCHEDULE AT '2026-01-18 21:11:36' ON COMPLETION PRESERVE DISABLE DO BEGIN
    DECLARE v_ngay DATE;
    SET v_ngay = CURRENT_DATE;

    INSERT INTO quy_cong_ty_chot_ngay (
        ngay_chot,
        tien_mat,
        tien_ngan_hang,
        tong_quy
    )
    SELECT
        v_ngay,

        IFNULL(SUM(CASE
            WHEN hinh_thuc = 'tien_mat' AND loai = 'thu' THEN so_tien
            WHEN hinh_thuc = 'tien_mat' AND loai = 'chi' THEN -so_tien
            ELSE 0
        END), 0),

        IFNULL(SUM(CASE
            WHEN hinh_thuc = 'chuyen_khoan' AND loai = 'thu' THEN so_tien
            WHEN hinh_thuc = 'chuyen_khoan' AND loai = 'chi' THEN -so_tien
            ELSE 0
        END), 0),

        IFNULL(SUM(CASE
            WHEN loai = 'thu' THEN so_tien
            WHEN loai = 'chi' THEN -so_tien
            ELSE 0
        END), 0)

    FROM thu_chi
    WHERE doi_tuong = 'cong_ty'
      AND DATE(ngay) <= v_ngay

    ON DUPLICATE KEY UPDATE
        ngay_tao = ngay_tao;
END//
DELIMITER ;

-- Dumping structure for event ctvt3.ev_chot_quy_nhan_vien_ngay
DELIMITER //
CREATE EVENT `ev_chot_quy_nhan_vien_ngay` ON SCHEDULE AT '2026-01-18 21:11:36' ON COMPLETION PRESERVE DISABLE DO BEGIN
    DECLARE v_ngay DATE;
    SET v_ngay = CURRENT_DATE;

    INSERT INTO quy_nhan_vien_chot_ngay (
        ngay_chot,
        ma_nv,
        so_du
    )
    SELECT
        v_ngay,
        ma_nv,
        IFNULL(SUM(CASE
            WHEN loai = 'thu' THEN so_tien
            WHEN loai = 'chi' THEN -so_tien
            ELSE 0
        END), 0)

    FROM thu_chi
    WHERE doi_tuong = 'nhan_vien'
      AND DATE(ngay) <= v_ngay

    GROUP BY ma_nv

    ON DUPLICATE KEY UPDATE
        ngay_tao = ngay_tao;
END//
DELIMITER ;

-- Dumping structure for table ctvt3.gas_du
CREATE TABLE IF NOT EXISTS `gas_du` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` date DEFAULT NULL,
  `ma_kh` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_kg_du` decimal(10,2) DEFAULT NULL,
  `don_gia` decimal(18,2) DEFAULT NULL,
  `tien_quy_doi` decimal(18,2) DEFAULT NULL,
  `id_hoa_don_ban` int DEFAULT NULL,
  `trang_thai` enum('chua_xu_ly','da_tra_ncc') COLLATE utf8mb4_unicode_ci DEFAULT 'chua_xu_ly',
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_hoa_don_ban` (`id_hoa_don_ban`),
  CONSTRAINT `gas_du_ibfk_1` FOREIGN KEY (`id_hoa_don_ban`) REFERENCES `hoa_don_ban` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.gas_du: ~0 rows (approximately)

-- Dumping structure for table ctvt3.gas_du_chot_ngay
CREATE TABLE IF NOT EXISTS `gas_du_chot_ngay` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` date DEFAULT NULL,
  `tong_kg` decimal(12,2) DEFAULT NULL,
  `tong_tien` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_gasdu` (`ngay`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.gas_du_chot_ngay: ~0 rows (approximately)

-- Dumping structure for table ctvt3.hoa_don_ban
CREATE TABLE IF NOT EXISTS `hoa_don_ban` (
  `id` int NOT NULL AUTO_INCREMENT,
  `so_hd` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay` date DEFAULT NULL,
  `ma_kh` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tong_tien` decimal(18,2) DEFAULT NULL,
  `tien_mat` decimal(18,2) DEFAULT NULL,
  `tien_ck` decimal(18,2) DEFAULT NULL,
  `tong_thanh_toan` decimal(18,2) DEFAULT NULL,
  `no_lai` decimal(18,2) DEFAULT NULL,
  `trang_thai` enum('nhap','xac_nhan','chot','huy') COLLATE utf8mb4_unicode_ci DEFAULT 'nhap',
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ma_kh` (`ma_kh`),
  KEY `ma_nv` (`ma_nv`),
  KEY `ma_kho` (`ma_kho`),
  CONSTRAINT `hoa_don_ban_ibfk_1` FOREIGN KEY (`ma_kh`) REFERENCES `khach_hang` (`ma_kh`),
  CONSTRAINT `hoa_don_ban_ibfk_2` FOREIGN KEY (`ma_nv`) REFERENCES `nhan_vien` (`ma_nv`),
  CONSTRAINT `hoa_don_ban_ibfk_3` FOREIGN KEY (`ma_kho`) REFERENCES `kho_hang` (`ma_kho`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.hoa_don_ban: ~0 rows (approximately)

-- Dumping structure for table ctvt3.hoa_don_ban_chi_tiet
CREATE TABLE IF NOT EXISTS `hoa_don_ban_chi_tiet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_hoa_don` int NOT NULL,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_luong` decimal(10,2) DEFAULT NULL,
  `don_gia` decimal(18,2) DEFAULT NULL,
  `thanh_tien` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_hoa_don` (`id_hoa_don`),
  KEY `ma_sp` (`ma_sp`),
  CONSTRAINT `hoa_don_ban_chi_tiet_ibfk_1` FOREIGN KEY (`id_hoa_don`) REFERENCES `hoa_don_ban` (`id`),
  CONSTRAINT `hoa_don_ban_chi_tiet_ibfk_2` FOREIGN KEY (`ma_sp`) REFERENCES `san_pham` (`ma_sp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.hoa_don_ban_chi_tiet: ~0 rows (approximately)

-- Dumping structure for table ctvt3.hoa_don_nhap
CREATE TABLE IF NOT EXISTS `hoa_don_nhap` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` date DEFAULT NULL,
  `ma_ncc` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tong_tien` decimal(18,2) DEFAULT NULL,
  `tien_mat` decimal(18,2) DEFAULT NULL,
  `tien_ck` decimal(18,2) DEFAULT NULL,
  `tong_thanh_toan` decimal(18,2) DEFAULT NULL,
  `trang_thai` enum('nhap','xac_nhan','chot','huy') COLLATE utf8mb4_unicode_ci DEFAULT 'nhap',
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ma_ncc` (`ma_ncc`),
  KEY `ma_nv` (`ma_nv`),
  KEY `ma_kho` (`ma_kho`),
  CONSTRAINT `hoa_don_nhap_ibfk_1` FOREIGN KEY (`ma_ncc`) REFERENCES `nha_cung_cap` (`ma_ncc`),
  CONSTRAINT `hoa_don_nhap_ibfk_2` FOREIGN KEY (`ma_nv`) REFERENCES `nhan_vien` (`ma_nv`),
  CONSTRAINT `hoa_don_nhap_ibfk_3` FOREIGN KEY (`ma_kho`) REFERENCES `kho_hang` (`ma_kho`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.hoa_don_nhap: ~0 rows (approximately)

-- Dumping structure for table ctvt3.hoa_don_nhap_chi_tiet
CREATE TABLE IF NOT EXISTS `hoa_don_nhap_chi_tiet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_hoa_don` int NOT NULL,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_luong` decimal(10,2) DEFAULT NULL,
  `don_gia` decimal(18,2) DEFAULT NULL,
  `thanh_tien` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_hoa_don` (`id_hoa_don`),
  KEY `ma_sp` (`ma_sp`),
  CONSTRAINT `hoa_don_nhap_chi_tiet_ibfk_1` FOREIGN KEY (`id_hoa_don`) REFERENCES `hoa_don_nhap` (`id`),
  CONSTRAINT `hoa_don_nhap_chi_tiet_ibfk_2` FOREIGN KEY (`ma_sp`) REFERENCES `san_pham` (`ma_sp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.hoa_don_nhap_chi_tiet: ~0 rows (approximately)

-- Dumping structure for table ctvt3.hoa_don_vat
CREATE TABLE IF NOT EXISTS `hoa_don_vat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `loai` enum('dau_vao','dau_ra','can_thue') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_hd_vat` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay` date DEFAULT NULL,
  `tien_truoc_thue` decimal(18,2) DEFAULT NULL,
  `tien_thue` decimal(18,2) DEFAULT NULL,
  `tong_tien` decimal(18,2) DEFAULT NULL,
  `bang_tham_chieu` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_tham_chieu` int DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  `trang_thai` enum('nhap','ghi_nhan') COLLATE utf8mb4_unicode_ci DEFAULT 'ghi_nhan',
  `nguoi_tao` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.hoa_don_vat: ~0 rows (approximately)

-- Dumping structure for table ctvt3.khach_hang
CREATE TABLE IF NOT EXISTS `khach_hang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_kh` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ten_cua_hang` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dia_chi` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_dien_thoai` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_so_thue` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ghi_chu` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ma_kh` (`ma_kh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.khach_hang: ~0 rows (approximately)

-- Dumping structure for table ctvt3.kho_hang
CREATE TABLE IF NOT EXISTS `kho_hang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ten_kho` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ma_kho` (`ma_kho`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.kho_hang: ~0 rows (approximately)

-- Dumping structure for table ctvt3.nha_cung_cap
CREATE TABLE IF NOT EXISTS `nha_cung_cap` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_ncc` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ten_ncc` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dia_chi` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_dien_thoai` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_so_thue` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ghi_chu` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ma_ncc` (`ma_ncc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.nha_cung_cap: ~0 rows (approximately)

-- Dumping structure for table ctvt3.nhan_vien
CREATE TABLE IF NOT EXISTS `nhan_vien` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ten_nv` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vai_tro` enum('admin','ke_toan','nv_dac_biet','nhan_vien','ke_toan_online') COLLATE utf8mb4_unicode_ci NOT NULL,
  `trang_thai` enum('hoat_dong','ngung') COLLATE utf8mb4_unicode_ci DEFAULT 'hoat_dong',
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ma_nv` (`ma_nv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.nhan_vien: ~0 rows (approximately)

-- Dumping structure for table ctvt3.nhan_vien_kho
CREATE TABLE IF NOT EXISTS `nhan_vien_kho` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_nv_kho` (`ma_nv`,`ma_kho`),
  KEY `ma_kho` (`ma_kho`),
  CONSTRAINT `nhan_vien_kho_ibfk_1` FOREIGN KEY (`ma_nv`) REFERENCES `nhan_vien` (`ma_nv`),
  CONSTRAINT `nhan_vien_kho_ibfk_2` FOREIGN KEY (`ma_kho`) REFERENCES `kho_hang` (`ma_kho`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.nhan_vien_kho: ~0 rows (approximately)

-- Dumping structure for table ctvt3.nhat_ky_kho
CREATE TABLE IF NOT EXISTS `nhat_ky_kho` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` datetime DEFAULT NULL,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_luong` decimal(10,2) DEFAULT NULL,
  `loai` enum('nhap','xuat') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bang_tham_chieu` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_tham_chieu` int DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.nhat_ky_kho: ~0 rows (approximately)

-- Dumping structure for table ctvt3.nhat_ky_vo
CREATE TABLE IF NOT EXISTS `nhat_ky_vo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` datetime DEFAULT NULL,
  `ma_kh` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `loai_vo` enum('12kg','45kg','mini') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_luong` int DEFAULT NULL,
  `loai` enum('giao','thu') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bang_tham_chieu` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_tham_chieu` int DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.nhat_ky_vo: ~0 rows (approximately)

-- Dumping structure for table ctvt3.quy_cong_ty_chot_ngay
CREATE TABLE IF NOT EXISTS `quy_cong_ty_chot_ngay` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay_chot` date NOT NULL,
  `tien_mat` decimal(18,2) NOT NULL,
  `tien_ngan_hang` decimal(18,2) NOT NULL,
  `tong_quy` decimal(18,2) NOT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_quy_ct_ngay` (`ngay_chot`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.quy_cong_ty_chot_ngay: ~0 rows (approximately)
REPLACE INTO `quy_cong_ty_chot_ngay` (`id`, `ngay_chot`, `tien_mat`, `tien_ngan_hang`, `tong_quy`, `ngay_tao`) VALUES
	(1, '2026-01-18', 0.00, 0.00, 0.00, '2026-01-18 21:11:36');

-- Dumping structure for table ctvt3.quy_nhan_vien_chot_ngay
CREATE TABLE IF NOT EXISTS `quy_nhan_vien_chot_ngay` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay_chot` date NOT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `so_du` decimal(18,2) NOT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_quy_nv_ngay` (`ngay_chot`,`ma_nv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.quy_nhan_vien_chot_ngay: ~0 rows (approximately)

-- Dumping structure for table ctvt3.san_pham
CREATE TABLE IF NOT EXISTS `san_pham` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ten_sp` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `loai_san_pham` enum('gas_binh','gas_kg','gas_mini','khac') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `don_vi_tinh` enum('binh','kg','lon','cai') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dung_tich_kg` decimal(6,2) DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ma_sp` (`ma_sp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.san_pham: ~0 rows (approximately)

-- Dumping structure for table ctvt3.thu_chi
CREATE TABLE IF NOT EXISTS `thu_chi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` datetime DEFAULT NULL,
  `doi_tuong` enum('nhan_vien','cong_ty') COLLATE utf8mb4_unicode_ci NOT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_tien` decimal(18,2) DEFAULT NULL,
  `loai` enum('thu','chi') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hinh_thuc` enum('tien_mat','chuyen_khoan') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `noi_dung` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ma_nv` (`ma_nv`),
  CONSTRAINT `thu_chi_ibfk_1` FOREIGN KEY (`ma_nv`) REFERENCES `nhan_vien` (`ma_nv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.thu_chi: ~0 rows (approximately)

-- Dumping structure for table ctvt3.thu_ngan
CREATE TABLE IF NOT EXISTS `thu_ngan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` date DEFAULT NULL,
  `ma_nv` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_tien` decimal(18,2) DEFAULT NULL,
  `ghi_chu` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ngay_tao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ma_nv` (`ma_nv`),
  CONSTRAINT `thu_ngan_ibfk_1` FOREIGN KEY (`ma_nv`) REFERENCES `nhan_vien` (`ma_nv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.thu_ngan: ~0 rows (approximately)

-- Dumping structure for table ctvt3.ton_kho_chot_ngay
CREATE TABLE IF NOT EXISTS `ton_kho_chot_ngay` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay` date DEFAULT NULL,
  `ma_kho` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ma_sp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `so_luong` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_chot` (`ngay`,`ma_kho`,`ma_sp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table ctvt3.ton_kho_chot_ngay: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
