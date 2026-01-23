# core/entities/hoa_don_nhap.py

from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from core.enums.trang_thai_chung_tu import TrangThaiChungTu


class HoaDonNhap:
    """
    ENTITY: hoa_don_nhap

    Vai trò:
    - Mapping 1–1 bảng hoa_don_nhap trong DB
    - Đại diện cho hóa đơn nhập gas
    - KHÔNG chứa logic nghiệp vụ
    - KHÔNG tự sinh hệ quả (kho, công nợ, VAT)
    """

    def __init__(
        self,
        id: int,
        ngay: Optional[date],
        ma_ncc: Optional[str],
        ma_nv: Optional[str],
        ma_kho: Optional[str],
        tong_tien: Optional[Decimal],
        tien_mat: Optional[Decimal],
        tien_ck: Optional[Decimal],
        tong_thanh_toan: Optional[Decimal],
        trang_thai: TrangThaiChungTu,
        ngay_tao: datetime,
    ):
        self.id = id
        self.ngay = ngay
        self.ma_ncc = ma_ncc
        self.ma_nv = ma_nv
        self.ma_kho = ma_kho
        self.tong_tien = tong_tien
        self.tien_mat = tien_mat
        self.tien_ck = tien_ck
        self.tong_thanh_toan = tong_thanh_toan
        self.trang_thai = trang_thai
        self.ngay_tao = ngay_tao
