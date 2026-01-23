# modules/nhap_gas/commands/them_chi_tiet_nhap.py

class ThemChiTietNhap:
    """
    Ý định: thêm chi tiết nhập vào hóa đơn nhập
    """

    def __init__(self, hoa_don_id: str, san_pham_id: str, so_luong, don_gia):
        self.hoa_don_id = hoa_don_id
        self.san_pham_id = san_pham_id
        self.so_luong = so_luong
        self.don_gia = don_gia
