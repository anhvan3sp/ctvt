# modules/thu_chi/events/phieu_chi_da_ghi_nhan.py

from core.value_objects.thoi_diem import ThoiDiem
from core.value_objects.so_tien import SoTien


class PhieuChiDaGhiNhan:
    """
    Sự kiện: phiếu chi đã được ghi nhận
    """

    def __init__(self, doi_tuong_id: str, so_tien: SoTien, thoi_diem: ThoiDiem):
        self.doi_tuong_id = doi_tuong_id
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem

    def __repr__(self):
        return f"PhieuChiDaGhiNhan(doi_tuong_id={self.doi_tuong_id}, so_tien={self.so_tien})"
