

from decimal import Decimal
from typing import Optional


class HoaDonBanChiTiet:
    """
    ENTITY: hoa_don_ban_chi_tiet

    Vai trò:
    - Mapping 1–1 bảng hoa_don_ban_chi_tiet trong DB
    - Mỗi instance = 1 dòng chi tiết bán hàng
    - KHÔNG chứa logic nghiệp vụ
    - KHÔNG tự tính toán
    """

    def __init__(
        self,
        id: int,
        id_hoa_don: int,
        ma_sp: Optional[str],
        so_luong: Optional[Decimal],
        don_gia: Optional[Decimal],
        thanh_tien: Optional[Decimal],
    ):
        self.id = id
        self.id_hoa_don = id_hoa_don
        self.ma_sp = ma_sp
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.thanh_tien = thanh_tien
