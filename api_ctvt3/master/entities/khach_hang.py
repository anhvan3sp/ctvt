from dataclasses import dataclass
from typing import Optional
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong
from master.enums.loai_khach_hang import LoaiKhachHang


@dataclass
class KhachHang:
    id: int
    ma_khach_hang: str
    ten_khach_hang: str
    loai_khach_hang: LoaiKhachHang
    trang_thai: TrangThaiDoiTuong
    ghi_chu: Optional[str] = None
