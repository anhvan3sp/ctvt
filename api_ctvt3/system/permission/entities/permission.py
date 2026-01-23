from dataclasses import dataclass


@dataclass
class Permission:
    id: int
    ma_permission: str
    mo_ta: str
