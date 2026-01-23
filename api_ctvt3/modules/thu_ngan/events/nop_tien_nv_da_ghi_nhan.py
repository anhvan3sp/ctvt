# modules/thu_ngan/events/nop_tien_nv_da_ghi_nhan.py

from core.value_objects.so_tien import SoTien
from core.value_objects.thoi_diem import ThoiDiem


class NopTienNhanVienDaGhiNhan:
    """
    Sự kiện: nhân viên đã nộp tiền về quỹ
    """

    def __init__(self, nhan_vien_id: str, so_tien: SoTien, thoi_diem: ThoiDiem):
        self.nhan_vien_id = nhan_vien_id
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem
