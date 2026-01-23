# modules/nhap_gas/events/hoa_don_nhap_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem


class HoaDonNhapDaGhiNhan:
    """
    Sự kiện: hóa đơn nhập đã được ghi nhận (đã chốt)
    """

    def __init__(self, hoa_don_id: str, thoi_diem: ThoiDiem):
        self.hoa_don_id = hoa_don_id
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return f"HoaDonNhapDaGhiNhan(hoa_don_id={self.hoa_don_id})"
