# modules/ke_toan/commands/tao_hoa_don_vat_can_thue.py

class TaoHoaDonVatCanThue:
    """
    Ý định: tạo hóa đơn VAT cần kê khai
    """

    def __init__(self, chung_tu_id: str, thoi_diem):
        self.chung_tu_id = chung_tu_id
        self.thoi_diem = thoi_diem
