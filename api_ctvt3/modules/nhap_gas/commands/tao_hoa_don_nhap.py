# modules/nhap_gas/commands/tao_hoa_don_nhap.py

class TaoHoaDonNhap:
    """
    Ý định: tạo hóa đơn nhập gas
    """

    def __init__(self, nha_cung_cap_id: str, ngay_lap):
        self.nha_cung_cap_id = nha_cung_cap_id
        self.ngay_lap = ngay_lap
