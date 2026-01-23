# modules/nhap_gas/services/nhap_gas_service.py

from core.entities.hoa_don_nhap import HoaDonNhap
from core.enums.trang_thai_chung_tu import TrangThaiChungTu
from core.rules.hoa_don_rules import HoaDonRules
from modules.nhap_gas.rules.nhap_gas_rules import NhapGasRules
from modules.nhap_gas.events.hoa_don_nhap_da_ghi_nhan import HoaDonNhapDaGhiNhan


class NhapGasService:
    def __init__(self, hoa_don_repo):
        self.hoa_don_repo = hoa_don_repo

    def tao_hoa_don(self, command):
        hoa_don = HoaDonNhap(
            nha_cung_cap_id=command.nha_cung_cap_id,
            ngay_lap=command.ngay_lap,
            trang_thai=TrangThaiChungTu.NHAP,
        )
        self.hoa_don_repo.save(hoa_don)
        return hoa_don

    def them_chi_tiet(self, command):
        hoa_don = self.hoa_don_repo.get_by_id(command.hoa_don_id)

        if not NhapGasRules.duoc_them_chi_tiet(hoa_don.trang_thai):
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

        event = HoaDonNhapDaGhiNhan(
            hoa_don_id=hoa_don.id,
            thoi_diem=command.thoi_diem,
        )

        return event
