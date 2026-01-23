# modules/ban_gas/rules/kiem_soat_thanh_toan.py

from core.value_objects.so_tien import SoTien


class KiemSoatThanhToan:
    @staticmethod
    def so_tien_hop_le(so_tien: SoTien) -> bool:
        return so_tien.gia_tri > 0
