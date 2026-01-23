# core/enums/loai_thu_chi.py

from enum import Enum


class LoaiThuChi(str, Enum):
    """
    Phân loại phiếu thu / chi
    """

    THU = "thu"
    CHI = "chi"
