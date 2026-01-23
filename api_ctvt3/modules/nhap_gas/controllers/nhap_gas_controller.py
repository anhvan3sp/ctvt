# modules/nhap_gas/controllers/nhap_gas_controller.py

from modules.nhap_gas.commands.tao_hoa_don_nhap import TaoHoaDonNhap
from modules.nhap_gas.commands.them_chi_tiet_nhap import ThemChiTietNhap
from modules.nhap_gas.commands.xac_nhan_hoa_don_nhap import XacNhanHoaDonNhap
from modules.nhap_gas.services.nhap_gas_service import NhapGasService


class NhapGasController:
    def __init__(self, service: NhapGasService):
        self.service = service

    def tao_hoa_don(self, data: dict):
        command = TaoHoaDonNhap(**data)
        return self.service.tao_hoa_don(command)

    def them_chi_tiet(self, data: dict):
        command = ThemChiTietNhap(**data)
        return self.service.them_chi_tiet(command)

    def xac_nhan_hoa_don(self, data: dict):
        command = XacNhanHoaDonNhap(**data)
        return self.service.xac_nhan_hoa_don(command)
