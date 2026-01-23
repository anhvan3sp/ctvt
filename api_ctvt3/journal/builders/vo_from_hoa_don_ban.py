from journal.entities.nhat_ky_vo import NhatKyVo
from journal.enums.loai_nhat_ky_vo import LoaiNhatKyVo


class VoFromHoaDonBan:
    @staticmethod
    def build(hoa_don_ban, thoi_diem):
        return NhatKyVo(
            chung_tu_id=hoa_don_ban.id,
            so_luong_vo=len(hoa_don_ban.chi_tiet),
            loai_nhat_ky=LoaiNhatKyVo.GIAM_VO,
            thoi_diem=thoi_diem,
        )
