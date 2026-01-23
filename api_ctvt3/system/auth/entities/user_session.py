from dataclasses import dataclass
from system.enums.trang_thai_phien import TrangThaiPhien
from system.auth.enums.loai_phien import LoaiPhien


@dataclass
class UserSession:
    id: int
    user_id: int
    token: str
    loai_phien: LoaiPhien
    trang_thai: TrangThaiPhien
