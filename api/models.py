from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    Numeric, Text, Enum
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# =========================
# SAN PHAM
# =========================
class SanPham(Base):
    __tablename__ = "san_pham"

    id = Column(Integer, primary_key=True)
    ma_sp = Column(String(50), unique=True, nullable=False)
    ten_sp = Column(String(255), nullable=False)


# =========================
# KHO HANG
# =========================
class KhoHang(Base):
    __tablename__ = "kho_hang"

    id = Column(Integer, primary_key=True)
    ma_kho = Column(String(20), unique=True, nullable=False)
    ten_kho = Column(String(255), nullable=False)


# =========================
# NHAN VIEN
# =========================
class NhanVien(Base):
    __tablename__ = "nhan_vien"

    id = Column(Integer, primary_key=True)
    ma_nv = Column(String(50), unique=True, nullable=False)
    ten_nv = Column(String(255), nullable=False)
    sdt = Column(String(20))
    vai_tro = Column(String(50))
    trang_thai = Column(String(20))


# =========================
# KHACH HANG
# =========================
class KhachHang(Base):
    __tablename__ = "khach_hang"

    id = Column(Integer, primary_key=True)
    ma_kh = Column(String(50), unique=True, nullable=False)
    ten_kh = Column(String(255), nullable=False)
    ten_khach_bi_danh = Column(String(100))
    dia_chi = Column(String(255))
    sdt = Column(String(20))
    mst = Column(String(20))


# =========================
# NHA CUNG CAP
# =========================
class NhaCungCap(Base):
    __tablename__ = "nha_cung_cap"

    id = Column(Integer, primary_key=True)
    ma_ncc = Column(String(50), unique=True, nullable=False)
    ten_ncc = Column(String(255), nullable=False)
    dia_chi = Column(String(255))
    sdt = Column(String(20))
    mst = Column(String(20))


# =========================
# HOA DON BAN
# =========================
class HoaDonBan(Base):
    __tablename__ = "hoa_don_ban"

    id = Column(Integer, primary_key=True)
    ngay = Column(Date, nullable=False)
    so_hd = Column(String(50))

    ma_kh = Column(String(50), nullable=False)
    ma_sp = Column(String(50), nullable=False)
    ma_kho = Column(String(20), nullable=False)
    ma_nv = Column(String(50), nullable=False)

    so_luong = Column(Numeric(10, 2), nullable=False)
    gia = Column(Numeric(18, 2), nullable=False)

    tien_mat = Column(Numeric(18, 2))
    tien_ck = Column(Numeric(18, 2))
    no_lai = Column(Numeric(18, 2))

    thanh_tien = Column(Numeric(18, 2))
    vat_amount = Column(Numeric(18, 2))

    so_vo_giao = Column(Integer, default=0)
    so_vo_thu = Column(Integer, default=0)

    ghi_chu = Column(Text)


# =========================
# HOA DON NHAP
# =========================
class HoaDonNhap(Base):
    __tablename__ = "hoa_don_nhap"

    id = Column(Integer, primary_key=True)
    ngay = Column(Date, nullable=False)

    ma_ncc = Column(String(50), nullable=False)
    ma_sp = Column(String(50), nullable=False)
    ma_kho = Column(String(20), nullable=False)
    ma_nv = Column(String(50), nullable=False)

    so_luong = Column(Numeric(10, 2), nullable=False)
    gia = Column(Numeric(18, 2), nullable=False)

    tien_mat = Column(Numeric(18, 2))
    tien_ck = Column(Numeric(18, 2))
    no_lai = Column(Numeric(18, 2))

    thanh_tien = Column(Numeric(18, 2))
    vat_amount = Column(Numeric(18, 2))

    ghi_chu = Column(Text)


# =========================
# THU CHI
# =========================
class ThuChi(Base):
    __tablename__ = "thu_chi"

    id = Column(Integer, primary_key=True)
    ngay = Column(Date, nullable=False)
    ma_nv = Column(String(50))

    so_tien = Column(Numeric(18, 2), nullable=False)
    hinh_thuc = Column(String(20))   # tien_mat | chuyen_khoan
    loai_gd = Column(String(10))     # thu | chi

    danh_muc = Column(String(100))
    noi_dung = Column(String(255))
# =========================
# DON DAT HANG BAN
# =========================
class DonDatHangBan(Base):
    __tablename__ = "don_dat_hang_ban"

    id = Column(Integer, primary_key=True)
    ma_don = Column(String(50), unique=True, nullable=False)
    ma_kh = Column(String(50), nullable=False)
    ngay_dat = Column(Date, nullable=False)

    tong_tien_du_kien = Column(Numeric(18, 2), nullable=False)
    tien_da_thu = Column(Numeric(18, 2), default=0)

    trang_thai = Column(
        String(20),
        default="dat_hang"
    )

    ghi_chu = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


# =========================
# DON DAT HANG NHAP
# =========================
class DonDatHangNhap(Base):
    __tablename__ = "don_dat_hang_nhap"

    id = Column(Integer, primary_key=True)
    ma_don = Column(String(50), unique=True, nullable=False)
    ma_ncc = Column(String(50), nullable=False)
    ngay_dat = Column(Date, nullable=False)

    tong_tien_du_kien = Column(Numeric(18, 2), nullable=False)
    tien_da_chi = Column(Numeric(18, 2), default=0)

    trang_thai = Column(
        String(20),
        default="dat_hang"
    )

    ghi_chu = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

