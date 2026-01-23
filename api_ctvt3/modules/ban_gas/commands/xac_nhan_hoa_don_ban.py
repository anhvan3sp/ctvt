# modules/ban_gas/commands/xac_nhan_hoa_don_ban.py

class XacNhanHoaDonBan:
    """
    Ý định: xác nhận (chốt) hóa đơn bán
    """

    def __init__(self, hoa_don_id: str, thoi_diem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem
