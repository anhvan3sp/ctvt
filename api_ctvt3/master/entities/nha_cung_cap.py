from dataclasses import dataclass
from typing import Optional
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong


@dataclass
class NhaCungCap:
    id: int
    ma_nha_cung_cap: str
    ten_nha_cung_cap: str
    trang_thai: TrangThaiDoiTuong
    ghi_chu: Optional[str] = None
