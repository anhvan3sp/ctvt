# modules/ban_gas/commands/tao_hoa_don_ban.py

class TaoHoaDonBan:
    """
    Ý định: tạo hóa đơn bán mới
    """

    def __init__(self, khach_hang_id: str, ngay_lap):
        self.khach_hang_id = khach_hang_id
        self.ngay_lap = ngay_lap
