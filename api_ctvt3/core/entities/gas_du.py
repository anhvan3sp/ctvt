# core/entities/gas_du.py

from decimal import Decimal
from datetime import date, datetime
from typing import Optional


class GasDu:
    """
    ENTITY: gas_du

    Vai trò:
    - Mapping 1–1 bảng gas_du trong DB
    - Đại diện cho lượng gas bán theo kg bị dư
    - Chỉ sinh từ hóa đơn bán
    - KHÔNG chứa logic xử lý gas dư
    """

    def __init__(
        self,
        id: int,
        ngay: Optional[date],
        ma_kh: Optional[str],
        ma_nv: Optional[str],
        ma_kho: Optional[str],
        ma_sp: Optional[str],
        so_kg_du: Optional[Decimal],
        don_gia: Optional[Decimal],
        tien_quy_doi: Optional[Decimal],
        id_hoa_don_ban: Optional[int],
        trang_thai: str,
        ngay_tao: datetime,
    ):
        self.id = id
        self.ngay = ngay
        self.ma_kh = ma_kh
        self.ma_nv = ma_nv
        self.ma_kho = ma_kho
        self.ma_sp = ma_sp
        self.so_kg_du = so_kg_du
        self.don_gia = don_gia
        self.tien_quy_doi = tien_quy_doi
        self.id_hoa_don_ban = id_hoa_don_ban
        self.trang_thai = trang_thai
        self.ngay_tao = ngay_tao
