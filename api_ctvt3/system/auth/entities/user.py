from dataclasses import dataclass
from system.auth.enums.trang_thai_user import TrangThaiUser


@dataclass
class User:
    id: int
    username: str
    password_hash: str
    trang_thai: TrangThaiUser
