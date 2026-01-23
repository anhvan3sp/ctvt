# core/enums/trang_thai_chung_tu.py

from enum import Enum


class TrangThaiChungTu(str, Enum):
    """
    Trạng thái chung cho chứng từ CORE:
    - hóa đơn bán
    - hóa đơn nhập
    - thu / chi
    - thu ngân
    - hóa đơn VAT (ghi nhận)
    """

    NHAP = "nhap"            # Nháp – chưa sinh số
    XAC_NHAN = "xac_nhan"    # Đã ghi nhận – BẮT ĐẦU sinh số
    CHOT = "chot"            # Đã chốt kỳ – khóa
    HUY = "huy"              # Hủy – không tính số
