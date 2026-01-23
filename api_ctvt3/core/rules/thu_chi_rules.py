# core/rules/thu_chi_rules.py

from core.enums.loai_thu_chi import LoaiThuChi
from core.value_objects.so_tien import SoTien


class ThuChiRules:
    @staticmethod
    def so_tien_hop_le(so_tien: SoTien) -> bool:
        """
        Số tiền thu / chi phải > 0
        """
        return so_tien.gia_tri > 0

    @staticmethod
    def loai_thu_chi_hop_le(loai: LoaiThuChi) -> bool:
        """
        Chỉ chấp nhận các loại thu chi đã định nghĩa
        """
        return loai in (LoaiThuChi.THU, LoaiThuChi.CHI)

    @staticmethod
    def duoc_ghi_nhan(so_tien: SoTien, loai: LoaiThuChi) -> bool:
        """
        Điều kiện tối thiểu để ghi nhận phiếu thu / chi
        """
        if not ThuChiRules.so_tien_hop_le(so_tien):
            return False
        if not ThuChiRules.loai_thu_chi_hop_le(loai):
            return False
        return True
