# core/value_objects/so_tien.py

from decimal import Decimal, ROUND_HALF_UP


class SoTien:
    """
    Giá trị tiền tệ trong nghiệp vụ.
    - Không cho None
    - Không cho kiểu dữ liệu lạ
    - Có thể cho âm hoặc không, tuỳ nghiệp vụ kiểm soát ở RULES
    """

    def __init__(self, gia_tri):
        if gia_tri is None:
            raise ValueError("Số tiền không được để trống")

        try:
            self._gia_tri = Decimal(gia_tri).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        except Exception:
            raise ValueError("Giá trị số tiền không hợp lệ")

    @property
    def gia_tri(self) -> Decimal:
        return self._gia_tri

    def lon_hon_0(self) -> bool:
        return self._gia_tri > 0

    def lon_hon_hoac_bang_0(self) -> bool:
        return self._gia_tri >= 0

    def __add__(self, other):
        if not isinstance(other, SoTien):
            raise TypeError("Chỉ cộng được với SoTien")
        return SoTien(self._gia_tri + other.gia_tri)

    def __sub__(self, other):
        if not isinstance(other, SoTien):
            raise TypeError("Chỉ trừ được với SoTien")
        return SoTien(self._gia_tri - other.gia_tri)

    def __repr__(self):
        return f"SoTien({self._gia_tri})"
