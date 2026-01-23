from dataclasses import dataclass
from typing import Optional
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong
from master.enums.loai_san_pham import LoaiSanPham
from master.enums.don_vi_tinh import DonViTinh


@dataclass
class SanPham:
    id: int
    ma_san_pham: str
    ten_san_pham: str
    loai_san_pham: LoaiSanPham
    don_vi_tinh: DonViTinh
    trang_thai: TrangThaiDoiTuong
    ghi_chu: Optional[str] = None
