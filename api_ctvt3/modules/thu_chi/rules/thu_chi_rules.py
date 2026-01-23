# modules/thu_chi/rules/thu_chi_rules.py

from core.value_objects.so_tien import SoTien


class ThuChiRules:
    @staticmethod
    def so_tien_hop_le(so_tien: SoTien) -> bool:
        """
        Phiếu thu / chi chỉ hợp lệ khi số tiền > 0
        """
        return so_tien.gia_tri > 0
