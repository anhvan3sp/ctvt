# core/events/phieu_chi_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem
from core.value_objects.so_tien import SoTien


class PhieuChiDaGhiNhan:
    """
    Sự kiện: Phiếu chi đã được ghi nhận
    """

    def __init__(self, phieu_chi_id: str, so_tien: SoTien, thoi_diem: ThoiDiem):
        self.phieu_chi_id = phieu_chi_id
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return (
            f"PhieuChiDaGhiNhan(phieu_chi_id={self.phieu_chi_id}, "
            f"so_tien={self.so_tien}, thoi_diem={self.thoi_diem})"
        )
