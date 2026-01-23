# modules/thu_chi/services/thu_chi_service.py

from core.rules.thu_chi_rules import ThuChiRules
from modules.thu_chi.events.phieu_thu_da_ghi_nhan import PhieuThuDaGhiNhan
from modules.thu_chi.events.phieu_chi_da_ghi_nhan import PhieuChiDaGhiNhan


class ThuChiService:
    def __init__(self):
        pass

    def ghi_nhan_phieu_thu(self, command):
        if not ThuChiRules.so_tien_hop_le(command.so_tien):
            raise Exception("Số tiền phiếu thu không hợp lệ")

        event = PhieuThuDaGhiNhan(
            doi_tuong_id=command.doi_tuong_id,
            so_tien=command.so_tien,
            thoi_diem=command.thoi_diem,
        )

        return event

    def ghi_nhan_phieu_chi(self, command):
        if not ThuChiRules.so_tien_hop_le(command.so_tien):
            raise Exception("Số tiền phiếu chi không hợp lệ")

        event = PhieuChiDaGhiNhan(
            doi_tuong_id=command.doi_tuong_id,
            so_tien=command.so_tien,
            thoi_diem=command.thoi_diem,
        )

        return event
