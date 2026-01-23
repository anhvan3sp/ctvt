from dataclasses import dataclass
from system.audit.enums.loai_hanh_dong import LoaiHanhDong
from system.audit.enums.doi_tuong_tac_dong import DoiTuongTacDong


@dataclass
class AuditLog:
    id: int
    user_id: int
    hanh_dong: LoaiHanhDong
    doi_tuong: DoiTuongTacDong
    doi_tuong_id: int
    ghi_chu: str
