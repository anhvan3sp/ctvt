from journal.entities.nhat_ky_kho import NhatKyKho
from journal.enums.loai_nhat_ky_kho import LoaiNhatKyKho


class KhoFromHoaDonBan:
    @staticmethod
    def build(hoa_don_ban, thoi_diem):
        danh_sach = []
        for ct in hoa_don_ban.chi_tiet:
            danh_sach.append(
                NhatKyKho(
                    chung_tu_id=hoa_don_ban.id,
                    san_pham_id=ct.san_pham_id,
                    so_luong=ct.so_luong,
                    loai_nhat_ky=LoaiNhatKyKho.XUAT_KHO,
                    thoi_diem=thoi_diem,
                )
            )
        return danh_sach
