# core/events/hoa_don_ban_da_chot.py

from core.value_objects.thoi_diem import ThoiDiem


class HoaDonBanDaChot:
    """
    Sự kiện: Hóa đơn bán đã được chốt (xác nhận)
    """

    def __init__(self, hoa_don_id: str, thoi_diem: ThoiDiem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return f"HoaDonBanDaChot(hoa_don_id={self.hoa_don_id}, thoi_diem={self.thoi_diem})"
