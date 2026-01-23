# modules/thu_ngan/services/thu_ngan_service.py

from modules.thu_ngan.rules.thu_ngan_rules import ThuNganRules
from modules.thu_ngan.events.nop_tien_nv_da_ghi_nhan import NopTienNhanVienDaGhiNhan


class ThuNganService:
    def ghi_nhan_nop_tien(self, command):
        if not ThuNganRules.so_tien_hop_le(command.so_tien):
            raise Exception("Số tiền nộp không hợp lệ")

        return NopTienNhanVienDaGhiNhan(
            nhan_vien_id=command.nhan_vien_id,
            so_tien=command.so_tien,
            thoi_diem=command.thoi_diem,
        )
