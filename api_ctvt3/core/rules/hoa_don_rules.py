# core/rules/hoa_don_rules.py

from core.enums.trang_thai_chung_tu import TrangThaiChungTu


class HoaDonRules:
    @staticmethod
    def duoc_sua(trang_thai: TrangThaiChungTu) -> bool:
        """
        Hóa đơn chỉ được sửa khi đang ở trạng thái NHÁP
        """
        return trang_thai == TrangThaiChungTu.NHAP

    @staticmethod
    def duoc_xac_nhan(trang_thai: TrangThaiChungTu) -> bool:
        """
        Hóa đơn chỉ được xác nhận khi đang ở trạng thái NHÁP
        """
        return trang_thai == TrangThaiChungTu.NHAP

    @staticmethod
    def duoc_huy(trang_thai: TrangThaiChungTu) -> bool:
        """
        Hóa đơn chỉ được huỷ khi chưa xác nhận
        """
        return trang_thai == TrangThaiChungTu.NHAP

    @staticmethod
    def duoc_thu_tien(trang_thai: TrangThaiChungTu) -> bool:
        """
        Chỉ được thu tiền khi hóa đơn đã được xác nhận
        """
        return trang_thai == TrangThaiChungTu.DA_XAC_NHAN
