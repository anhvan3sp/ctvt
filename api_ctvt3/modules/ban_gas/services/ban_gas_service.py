# modules/ban_gas/services/ban_gas_service.py

from core.entities.hoa_don_ban import HoaDonBan
from core.enums.trang_thai_chung_tu import TrangThaiChungTu
from core.rules.hoa_don_rules import HoaDonRules
from modules.ban_gas.rules.ban_gas_rules import BanGasRules
from modules.ban_gas.events.hoa_don_ban_da_ghi_nhan import HoaDonBanDaGhiNhan


class BanGasService:
    def __init__(self, hoa_don_repo):
        self.hoa_don_repo = hoa_don_repo

    def tao_hoa_don(self, command):
        hoa_don = HoaDonBan(
            khach_hang_id=command.khach_hang_id,
            ngay_lap=command.ngay_lap,
            trang_thai=TrangThaiChungTu.NHAP,
        )
        self.hoa_don_repo.save(hoa_don)
        return hoa_don

    def them_chi_tiet(self, command):
        hoa_don = self.hoa_don_repo.get_by_id(command.hoa_don_id)

        if not BanGasRules.duoc_them_chi_tiet(hoa_don.trang_thai):
            raise Exception("Không được thêm chi tiết khi hóa đơn đã chốt")

        hoa_don.them_chi_tiet(
            san_pham_id=command.san_pham_id,
            so_luong=command.so_luong,
            don_gia=command.don_gia,
        )

        self.hoa_don_repo.save(hoa_don)
        return hoa_don

    def xac_nhan_hoa_don(self, command):
        hoa_don = self.hoa_don_repo.get_by_id(command.hoa_don_id)

        if not HoaDonRules.duoc_xac_nhan(hoa_don.trang_thai):
            raise Exception("Hóa đơn không hợp lệ để xác nhận")

        hoa_don.trang_thai = TrangThaiChungTu.DA_XAC_NHAN
        self.hoa_don_repo.save(hoa_don)

        event = HoaDonBanDaGhiNhan(
            hoa_don_id=hoa_don.id,
            thoi_diem=command.thoi_diem,
        )

        return event
