# modules/thu_ngan/controllers/thu_ngan_controller.py

from modules.thu_ngan.commands.ghi_nhan_nop_tien import GhiNhanNopTien
from modules.thu_ngan.services.thu_ngan_service import ThuNganService


class ThuNganController:
    def __init__(self, service: ThuNganService):
        self.service = service

    def ghi_nhan_nop_tien(self, data: dict):
        command = GhiNhanNopTien(**data)
        return self.service.ghi_nhan_nop_tien(command)
