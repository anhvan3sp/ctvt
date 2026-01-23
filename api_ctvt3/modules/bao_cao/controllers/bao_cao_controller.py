# modules/bao_cao/controllers/bao_cao_controller.py

class BaoCaoController:
    def __init__(self, cong_no_reader, ton_kho_reader, loi_nhuan_reader, vat_reader):
        self.cong_no_reader = cong_no_reader
        self.ton_kho_reader = ton_kho_reader
        self.loi_nhuan_reader = loi_nhuan_reader
        self.vat_reader = vat_reader
