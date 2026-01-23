# modules/thu_ngan/rules/thu_ngan_rules.py

from core.value_objects.so_tien import SoTien


class ThuNganRules:
    @staticmethod
    def so_tien_hop_le(so_tien: SoTien) -> bool:
        return so_tien.gia_tri > 0
