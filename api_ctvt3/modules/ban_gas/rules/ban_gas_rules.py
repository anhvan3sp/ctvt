# modules/ban_gas/rules/ban_gas_rules.py

from core.enums.trang_thai_chung_tu import TrangThaiChungTu


class BanGasRules:
    @staticmethod
    def duoc_them_chi_tiet(trang_thai: TrangThaiChungTu) -> bool:
        return trang_thai == TrangThaiChungTu.NHAP

    @staticmethod
    def duoc_xac_nhan(trang_thai: TrangThaiChungTu) -> bool:
        return trang_thai == TrangThaiChungTu.NHAP
