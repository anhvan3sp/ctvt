from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal


# =====================================================
# 1. SAN PHAM
# =====================================================
class SanPhamBase(BaseModel):
    ma_sp: str
    ten_sp: str


class SanPhamCreate(SanPhamBase):
    pass


class SanPhamUpdate(SanPhamBase):
    pass


class SanPhamRead(SanPhamBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 2. KHO HANG
# =====================================================
class KhoHangBase(BaseModel):
    ma_kho: str
    ten_kho: str


class KhoHangCreate(KhoHangBase):
    pass


class KhoHangUpdate(KhoHangBase):
    pass


class KhoHangRead(KhoHangBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 3. NHAN VIEN
# =====================================================
class NhanVienBase(BaseModel):
    ma_nv: str
    ten_nv: str
    sdt: Optional[str] = None
    vai_tro: Optional[str] = None
    trang_thai: Optional[str] = None


class NhanVienCreate(NhanVienBase):
    pass


class NhanVienUpdate(NhanVienBase):
    pass


class NhanVienRead(NhanVienBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 4. KHACH HANG
# =====================================================
class KhachHangBase(BaseModel):
    ma_kh: str
    ten_kh: str
    ten_khach_bi_danh: Optional[str] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    mst: Optional[str] = None


class KhachHangCreate(KhachHangBase):
    pass


class KhachHangUpdate(BaseModel):
    ten_kh: Optional[str] = None
    ten_khach_bi_danh: Optional[str] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    mst: Optional[str] = None


class KhachHangRead(KhachHangBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 5. NHA CUNG CAP
# =====================================================
class NhaCungCapBase(BaseModel):
    ma_ncc: str
    ten_ncc: str
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    mst: Optional[str] = None


class NhaCungCapCreate(NhaCungCapBase):
    pass


class NhaCungCapUpdate(BaseModel):
    ten_ncc: Optional[str] = None
    dia_chi: Optional[str] = None
    sdt: Optional[str] = None
    mst: Optional[str] = None


class NhaCungCapRead(NhaCungCapBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 6. HOA DON BAN
# =====================================================
class HoaDonBanBase(BaseModel):
    ngay: date
    so_hd: Optional[str] = None

    ma_kh: str
    ma_sp: str
    ma_kho: str
    ma_nv: str

    so_luong: Decimal
    gia: Decimal

    tien_mat: Optional[Decimal] = None
    tien_ck: Optional[Decimal] = None
    no_lai: Optional[Decimal] = None

    ghi_chu: Optional[str] = None

    so_vo_giao: Optional[int] = 0
    so_vo_thu: Optional[int] = 0


class HoaDonBanCreate(HoaDonBanBase):
    pass


class HoaDonBanRead(HoaDonBanBase):
    id: int
    thanh_tien: Decimal
    vat_amount: Decimal

    class Config:
        from_attributes = True


# =====================================================
# 7. HOA DON NHAP
# =====================================================
class HoaDonNhapBase(BaseModel):
    ngay: date

    ma_ncc: str
    ma_sp: str
    ma_kho: str
    ma_nv: str

    so_luong: Decimal
    gia: Decimal

    tien_mat: Optional[Decimal] = None
    tien_ck: Optional[Decimal] = None
    no_lai: Optional[Decimal] = None

    ghi_chu: Optional[str] = None


class HoaDonNhapCreate(HoaDonNhapBase):
    pass


class HoaDonNhapRead(HoaDonNhapBase):
    id: int
    thanh_tien: Decimal
    vat_amount: Decimal

    class Config:
        from_attributes = True


# =====================================================
# 8. THU CHI
# =====================================================
class ThuChiBase(BaseModel):
    ngay: date
    ma_nv: Optional[str] = None

    so_tien: Decimal
    hinh_thuc: str          # tien_mat | chuyen_khoan
    loai_gd: str            # thu | chi

    danh_muc: Optional[str] = None
    noi_dung: Optional[str] = None


class ThuChiCreate(ThuChiBase):
    pass


class ThuChiRead(ThuChiBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# 9. DASHBOARD (VIEW v_dashboard_app)
# =====================================================
class DashboardRead(BaseModel):
    ngay: date
    doanh_thu_hom_nay: Decimal
    tien_mat_hom_nay: Decimal
    tien_ck_hom_nay: Decimal
    tong_no_khach: Decimal
    tong_no_vo: Decimal
    tong_ton_kho: Decimal
# =====================================================
# 10. AUTH / LOGIN
# =====================================================
class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    ma_nv: Optional[str] = None
    role: Optional[str] = None

