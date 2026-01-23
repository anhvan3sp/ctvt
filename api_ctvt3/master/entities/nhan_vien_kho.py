from dataclasses import dataclass
from master.enums.trang_thai_doi_tuong import TrangThaiDoiTuong


@dataclass
class NhanVienKho:
    id: int
    nhan_vien_id: int
    kho_id: int
    trang_thai: TrangThaiDoiTuong
