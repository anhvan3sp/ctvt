# modules/ke_toan/controllers/ke_toan_controller.py

from modules.ke_toan.commands.tao_hoa_don_vat_can_thue import TaoHoaDonVatCanThue
from modules.ke_toan.services.ke_toan_service import KeToanService


class KeToanController:
    def __init__(self, service: KeToanService):
        self.service = service

    def tao_hoa_don_vat(self, data: dict):
        command = TaoHoaDonVatCanThue(**data)
        return self.service.tao_hoa_don_vat(command)
