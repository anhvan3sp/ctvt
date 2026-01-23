from dataclasses import dataclass
from typing import Optional
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong


@dataclass
class KhoHang:
    id: int
    ma_kho: str
    ten_kho: str
    trang_thai: TrangThaiDoiTuong
    ghi_chu: Optional[str] = None
