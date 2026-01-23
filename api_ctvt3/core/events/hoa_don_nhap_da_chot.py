# core/events/hoa_don_nhap_da_chot.py

from core.value_objects.thoi_diem import ThoiDiem


class HoaDonNhapDaChot:
    """
    Sự kiện: Hóa đơn nhập đã được chốt
    """

    def __init__(self, hoa_don_id: str, thoi_diem: ThoiDiem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return f"HoaDonNhapDaChot(hoa_don_id={self.hoa_don_id}, thoi_diem={self.thoi_diem})"
