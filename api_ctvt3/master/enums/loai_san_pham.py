from enum import Enum


class LoaiSanPham(str, Enum):
    GAS = "GAS"
    VO_BINH = "VO_BINH"
    PHU_KIEN = "PHU_KIEN"
