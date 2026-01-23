# modules/ke_toan/events/hoa_don_vat_can_thue_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem


class HoaDonVatCanThueDaGhiNhan:
    """
    Sự kiện: hóa đơn VAT cần kê khai đã được ghi nhận
    """

    def __init__(self, chung_tu_id: str, thoi_diem: ThoiDiem):
        self.chung_tu_id = chung_tu_id
        self.thoi_diem = thoi_diem
