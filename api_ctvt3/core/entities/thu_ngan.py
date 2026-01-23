# core/entities/thu_ngan.py

from decimal import Decimal
from datetime import date, datetime
from typing import Optional


class ThuNgan:
    """
    ENTITY: thu_ngan

    Vai trò:
    - Mapping 1–1 bảng thu_ngan trong DB
    - Đại diện cho sự kiện nhân viên nộp tiền
    - KHÔNG tạo doanh thu
    - KHÔNG chứa logic nghiệp vụ
    """

    def __init__(
        self,
        id: int,
        ngay: Optional[date],
        ma_nv: Optional[str],
        so_tien: Optional[Decimal],
        ghi_chu: Optional[str],
        ngay_tao: datetime,
    ):
        self.id = id
        self.ngay = ngay
        self.ma_nv = ma_nv
        self.so_tien = so_tien
        self.ghi_chu = ghi_chu
        self.ngay_tao = ngay_tao
