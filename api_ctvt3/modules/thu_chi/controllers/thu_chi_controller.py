# modules/thu_chi/controllers/thu_chi_controller.py

from modules.thu_chi.commands.ghi_nhan_phieu_thu import GhiNhanPhieuThu
from modules.thu_chi.commands.ghi_nhan_phieu_chi import GhiNhanPhieuChi
from modules.thu_chi.services.thu_chi_service import ThuChiService


class ThuChiController:
    def __init__(self, service: ThuChiService):
        self.service = service

    def ghi_nhan_phieu_thu(self, data: dict):
        command = GhiNhanPhieuThu(**data)
        return self.service.ghi_nhan_phieu_thu(command)

    def ghi_nhan_phieu_chi(self, data: dict):
        command = GhiNhanPhieuChi(**data)
        return self.service.ghi_nhan_phieu_chi(command)
