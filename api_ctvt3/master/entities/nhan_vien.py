from dataclasses import dataclass
from typing import Optional
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong


@dataclass
class NhanVien:
    id: int
    ma_nhan_vien: str
    ten_nhan_vien: str
    trang_thai: TrangThaiDoiTuong
    ghi_chu: Optional[str] = None
