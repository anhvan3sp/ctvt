# modules/nhap_gas/rules/nhap_gas_rules.py

from core.enums.trang_thai_chung_tu import TrangThaiChungTu


class NhapGasRules:
    @staticmethod
    def duoc_them_chi_tiet(trang_thai: TrangThaiChungTu) -> bool:
        """
        Chỉ được thêm chi tiết khi hóa đơn đang ở trạng thái NHÁP
        """
        return trang_thai == TrangThaiChungTu.NHAP

    @staticmethod
    def duoc_xac_nhan(trang_thai: TrangThaiChungTu) -> bool:
        """
        Chỉ được xác nhận khi hóa đơn đang ở trạng thái NHÁP
        """
        return trang_thai == TrangThaiChungTu.NHAP
