# core/value_objects/thoi_diem.py

from datetime import datetime


class ThoiDiem:
    """
    Thời điểm nghiệp vụ.
    - Bắt buộc là datetime
    - Không dùng string trôi nổi trong core
    """

    def __init__(self, gia_tri: datetime):
        if not isinstance(gia_tri, datetime):
            raise ValueError("Thời điểm phải là datetime")

        self._gia_tri = gia_tri

    @property
    def gia_tri(self) -> datetime:
        return self._gia_tri

    def truoc(self, thoi_diem_khac: "ThoiDiem") -> bool:
        return self._gia_tri < thoi_diem_khac.gia_tri

    def sau(self, thoi_diem_khac: "ThoiDiem") -> bool:
        return self._gia_tri > thoi_diem_khac.gia_tri

    def __repr__(self):
        return f"ThoiDiem({self._gia_tri.isoformat()})"
