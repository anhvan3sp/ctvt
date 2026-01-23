# core/entities/hoa_don_vat.py

from decimal import Decimal
from datetime import date, datetime
from typing import Optional


class HoaDonVAT:
    """
    ENTITY: hoa_don_vat

    Vai trò:
    - Mapping 1–1 bảng hoa_don_vat trong DB
    - Đại diện cho sự kiện ghi nhận VAT (đầu vào / đầu ra / cân thuế)
    - Có thể gắn hoặc không gắn giao dịch bán/nhập
    - KHÔNG chứa logic tính thuế
    """

    def __init__(
        self,
        id: int,
        loai: str,
        so_hd_vat: Optional[str],
        ngay: Optional[date],
        tien_truoc_thue: Optional[Decimal],
        tien_thue: Optional[Decimal],
        tong_tien: Optional[Decimal],
        bang_tham_chieu: Optional[str],
        id_tham_chieu: Optional[int],
        ngay_tao: datetime,
        trang_thai: str,
        nguoi_tao: Optional[str],
    ):
        self.id = id
        self.loai = loai
        self.so_hd_vat = so_hd_vat
        self.ngay = ngay
        self.tien_truoc_thue = tien_truoc_thue
        self.tien_thue = tien_thue
        self.tong_tien = tong_tien
        self.bang_tham_chieu = bang_tham_chieu
        self.id_tham_chieu = id_tham_chieu
        self.ngay_tao = ngay_tao
        self.trang_thai = trang_thai
        self.nguoi_tao = nguoi_tao
