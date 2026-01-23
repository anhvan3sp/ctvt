# modules/nhap_gas/commands/xac_nhan_hoa_don_nhap.py

class XacNhanHoaDonNhap:
    """
    Ý định: xác nhận (chốt) hóa đơn nhập
    """

    def __init__(self, hoa_don_id: str, thoi_diem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem
