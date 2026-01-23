# modules/ban_gas/controllers/ban_gas_controller.py

from modules.ban_gas.commands.tao_hoa_don_ban import TaoHoaDonBan
from modules.ban_gas.commands.them_chi_tiet_ban import ThemChiTietBan
from modules.ban_gas.commands.xac_nhan_hoa_don_ban import XacNhanHoaDonBan
from modules.ban_gas.services.ban_gas_service import BanGasService


class BanGasController:
    def __init__(self, service: BanGasService):
        self.service = service

    def tao_hoa_don(self, data: dict):
        command = TaoHoaDonBan(**data)
        return self.service.tao_hoa_don(command)

    def them_chi_tiet(self, data: dict):
        command = ThemChiTietBan(**data)
        return self.service.them_chi_tiet(command)

    def xac_nhan_hoa_don(self, data: dict):
        command = XacNhanHoaDonBan(**data)
        return self.service.xac_nhan_hoa_don(command)
