# modules/thu_ngan/commands/ghi_nhan_nop_tien.py

class GhiNhanNopTien:
    """
    Ý định: nhân viên nộp tiền về quỹ công ty
    """

    def __init__(self, nhan_vien_id: str, so_tien, thoi_diem):
        self.nhan_vien_id = nhan_vien_id
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem
