# core/entities/hoa_don_ban.py

from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from core.enums.trang_thai_chung_tu import TrangThaiChungTu


class HoaDonBan:
    """
    ENTITY: hoa_don_ban
    Vai trò:
    - Mapping 1–1 bảng hoa_don_ban trong DB
    - KHÔNG chứa logic nghiệp vụ
    - KHÔNG tính toán
    """

    def __init__(
        self,
        id: int,
        so_hd: Optional[str],
        ngay: Optional[date],
        ma_kh: Optional[str],
        ma_nv: Optional[str],
        ma_kho: Optional[str],
        tong_tien: Optional[Decimal],
        tien_mat: Optional[Decimal],
        tien_ck: Optional[Decimal],
        tong_thanh_toan: Optional[Decimal],
        no_lai: Optional[Decimal],
        trang_thai: TrangThaiChungTu,
        ngay_tao: datetime,
    ):
        self.id = id
        self.so_hd = so_hd
        self.ngay = ngay
        self.ma_kh = ma_kh
        self.ma_nv = ma_nv
        self.ma_kho = ma_kho
        self.tong_tien = tong_tien
        self.tien_mat = tien_mat
        self.tien_ck = tien_ck
        self.tong_thanh_toan = tong_thanh_toan
        self.no_lai = no_lai
        self.trang_thai = trang_thai
        self.ngay_tao = ngay_tao
