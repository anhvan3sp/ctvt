# modules/ke_toan/services/ke_toan_service.py

from modules.ke_toan.rules.ke_toan_rules import KeToanRules
from modules.ke_toan.events.hoa_don_vat_can_thue_da_ghi_nhan import HoaDonVatCanThueDaGhiNhan


class KeToanService:
    def tao_hoa_don_vat(self, command):
        if not KeToanRules.duoc_tao_hoa_don_vat():
            raise Exception("Không đủ điều kiện tạo hóa đơn VAT")

        return HoaDonVatCanThueDaGhiNhan(
            chung_tu_id=command.chung_tu_id,
            thoi_diem=command.thoi_diem,
        )
