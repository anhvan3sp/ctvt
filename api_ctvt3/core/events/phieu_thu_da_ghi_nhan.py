# core/events/phieu_thu_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem
from core.value_objects.so_tien import SoTien


class PhieuThuDaGhiNhan:
    """
    Sự kiện: Phiếu thu đã được ghi nhận
    """

    def __init__(self, phieu_thu_id: str, so_tien: SoTien, thoi_diem: ThoiDiem):
        self.phieu_thu_id = phieu_thu_id
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return (
            f"PhieuThuDaGhiNhan(phieu_thu_id={self.phieu_thu_id}, "
            f"so_tien={self.so_tien}, thoi_diem={self.thoi_diem})"
        )
