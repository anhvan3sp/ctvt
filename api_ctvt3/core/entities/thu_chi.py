# core/entities/thu_chi.py

from decimal import Decimal
from datetime import datetime
from typing import Optional


class ThuChi:
    """
    ENTITY: thu_chi

    Vai trò:
    - Mapping 1–1 bảng thu_chi trong DB
    - Đại diện cho một sự kiện thu hoặc chi tiền
    - KHÔNG chứa logic nghiệp vụ
    - KHÔNG cập nhật số dư
    """

    def __init__(
        self,
        id: int,
        ngay: datetime,
        doi_tuong: str,
        ma_nv: Optional[str],
        so_tien: Optional[Decimal],
        loai: Optional[str],
        hinh_thuc: Optional[str],
        noi_dung: Optional[str],
        ngay_tao: datetime,
    ):
        self.id = id
        self.ngay = ngay
        self.doi_tuong = doi_tuong
        self.ma_nv = ma_nv
        self.so_tien = so_tien
        self.loai = loai
        self.hinh_thuc = hinh_thuc
        self.noi_dung = noi_dung
        self.ngay_tao = ngay_tao
