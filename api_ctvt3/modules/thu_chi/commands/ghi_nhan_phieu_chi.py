# modules/thu_chi/commands/ghi_nhan_phieu_chi.py

class GhiNhanPhieuChi:
    """
    Ý định: ghi nhận một phiếu chi
    """

    def __init__(self, doi_tuong_id: str, so_tien, thoi_diem):
        self.doi_tuong_id = doi_tuong_id   # nhà cung cấp / nhân viên
        self.so_tien = so_tien
        self.thoi_diem = thoi_diem
