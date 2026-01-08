from sqlalchemy.orm import Session
from sqlalchemy import text, or_

from models import (
    SanPham,
    KhoHang,
    NhanVien,
    KhachHang,
    NhaCungCap,
    HoaDonBan,
    HoaDonNhap,
    ThuChi,
)

from schemas import (
    SanPhamCreate,
    KhoHangCreate,
    NhanVienCreate,
    KhachHangCreate,
    NhaCungCapCreate,
    HoaDonBanCreate,
    HoaDonNhapCreate,
    ThuChiCreate,
)

# =====================================================
# SAN PHAM
# =====================================================

def get_san_pham(db: Session):
    return db.query(SanPham).all()


def create_san_pham(db: Session, data: SanPhamCreate):
    sp = SanPham(**data.model_dump())
    db.add(sp)
    db.commit()
    db.refresh(sp)
    return sp


# =====================================================
# KHO HANG
# =====================================================

def get_kho_hang(db: Session):
    return db.query(KhoHang).all()


def create_kho_hang(db: Session, data: KhoHangCreate):
    kho = KhoHang(**data.model_dump())
    db.add(kho)
    db.commit()
    db.refresh(kho)
    return kho


# =====================================================
# NHAN VIEN
# =====================================================

def get_nhan_vien(db: Session):
    return db.query(NhanVien).all()


def create_nhan_vien(db: Session, data: NhanVienCreate):
    nv = NhanVien(**data.model_dump())
    db.add(nv)
    db.commit()
    db.refresh(nv)
    return nv


# =====================================================
# KHACH HANG
# =====================================================

def get_khach_hang(db: Session):
    return db.query(KhachHang).all()


def get_khach_hang_by_id(db: Session, kh_id: int):
    return db.query(KhachHang).filter(KhachHang.id == kh_id).first()


def create_khach_hang(db: Session, data: KhachHangCreate):
    kh = KhachHang(**data.model_dump())
    db.add(kh)
    db.commit()
    db.refresh(kh)
    return kh


def search_khach_hang(db: Session, keyword: str):
    return (
        db.query(KhachHang)
        .filter(
            or_(
                KhachHang.ma_kh.like(f"%{keyword}%"),
                KhachHang.ten_kh.like(f"%{keyword}%"),
                KhachHang.ten_khach_bi_danh.like(f"%{keyword}%"),
                KhachHang.sdt.like(f"%{keyword}%"),
            )
        )
        .limit(20)
        .all()
    )


# =====================================================
# NHA CUNG CAP
# =====================================================

def get_nha_cung_cap(db: Session):
    return db.query(NhaCungCap).all()


def create_nha_cung_cap(db: Session, data: NhaCungCapCreate):
    ncc = NhaCungCap(**data.model_dump())
    db.add(ncc)
    db.commit()
    db.refresh(ncc)
    return ncc


# =====================================================
# HOA DON BAN
# =====================================================

def get_hoa_don_ban(db: Session):
    return db.query(HoaDonBan).order_by(HoaDonBan.id.desc()).all()


def create_hoa_don_ban(db: Session, data: HoaDonBanCreate):
    """
    Trigger trong DB sẽ:
    - kiểm tra tiền
    - trừ tồn kho
    - ghi nhật ký kho
    - ghi nhật ký vỏ
    - cập nhật công nợ
    """
    hd = HoaDonBan(**data.model_dump())
    db.add(hd)
    db.commit()
    db.refresh(hd)
    return hd


# =====================================================
# HOA DON NHAP
# =====================================================

def get_hoa_don_nhap(db: Session):
    return db.query(HoaDonNhap).order_by(HoaDonNhap.id.desc()).all()


def create_hoa_don_nhap(db: Session, data: HoaDonNhapCreate):
    hd = HoaDonNhap(**data.model_dump())
    db.add(hd)
    db.commit()
    db.refresh(hd)
    return hd


# =====================================================
# THU CHI
# =====================================================

def get_thu_chi(db: Session):
    return db.query(ThuChi).order_by(ThuChi.id.desc()).all()


def create_thu_chi(db: Session, data: ThuChiCreate):
    tc = ThuChi(**data.model_dump())
    db.add(tc)
    db.commit()
    db.refresh(tc)
    return tc


# =====================================================
# DASHBOARD (VIEW v_dashboard_app)
# =====================================================

def get_dashboard(db: Session):
    """
    Đọc dữ liệu dashboard từ VIEW v_dashboard_app
    """
    sql = text("SELECT * FROM v_dashboard_app")
    result = db.execute(sql).mappings().first()
    return result
