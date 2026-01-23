# core/value_objects/so_luong.py

from decimal import Decimal


class SoLuong:
    """
    Giá trị số lượng trong nghiệp vụ.
    - Không âm
    - Có thể là số lẻ (kg, m3)
    """

    def __init__(self, gia_tri):
        if gia_tri is None:
            raise ValueError("Số lượng không được để trống")

        try:
            value = Decimal(gia_tri)
        except Exception:
            raise ValueError("Giá trị số lượng không hợp lệ")

        if value < 0:
            raise ValueError("Số lượng không được âm")

        self._gia_tri = value

    @property
    def gia_tri(self) -> Decimal:
        return self._gia_tri

    def lon_hon_0(self) -> bool:
        return self._gia_tri > 0

    def __add__(self, other):
        if not isinstance(other, SoLuong):
            raise TypeError("Chỉ cộng được với SoLuong")
        return SoLuong(self._gia_tri + other.gia_tri)

    def __repr__(self):
        return f"SoLuong({self._gia_tri})"
