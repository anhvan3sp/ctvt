# core/enums/loai_vat.py

from enum import Enum


class LoaiVAT(str, Enum):
    """
    Phân loại VAT trong hệ thống
    """

    DAU_VAO = "dau_vao"      # VAT đầu vào (nhập hàng)
    DAU_RA = "dau_ra"        # VAT đầu ra (bán hàng)
    CAN_THUE = "can_thue"    # VAT cân thuế (kế toán dịch vụ)
