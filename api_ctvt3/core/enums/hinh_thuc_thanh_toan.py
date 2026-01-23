# core/enums/hinh_thuc_thanh_toan.py

from enum import Enum


class HinhThucThanhToan(str, Enum):
    """
    Hình thức thanh toán
    """

    TIEN_MAT = "tien_mat"           # Tiền mặt (két)
    CHUYEN_KHOAN = "chuyen_khoan"   # Chuyển khoản (ngân hàng)
