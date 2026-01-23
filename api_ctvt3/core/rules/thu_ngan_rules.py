# core/rules/thu_ngan_rules.py

from core.value_objects.so_tien import SoTien


class ThuNganRules:
    @staticmethod
    def duoc_nop_tien(so_tien: SoTien) -> bool:
        """
        Nhân viên chỉ được nộp tiền khi số tiền > 0
        """
        return so_tien.gia_tri > 0

    @staticmethod
    def duoc_giu_tien(so_tien: SoTien) -> bool:
        """
        Thu ngân chỉ được giữ tiền khi số tiền >= 0
        """
        return so_tien.gia_tri >= 0
