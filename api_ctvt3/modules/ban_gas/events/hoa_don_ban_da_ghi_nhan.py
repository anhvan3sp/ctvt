# modules/ban_gas/events/hoa_don_ban_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem


class HoaDonBanDaGhiNhan:
    """
    Sự kiện: hóa đơn bán đã được ghi nhận (chốt xong)
    """

    def __init__(self, hoa_don_id: str, thoi_diem: ThoiDiem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return f"HoaDonBanDaGhiNhan(hoa_don_id={self.hoa_don_id})"
