from master.validators.nhan_vien_validator import NhanVienValidator


class NhanVienService:
    def __init__(self, repo):
        self.repo = repo

    def tao_moi(self, data):
        NhanVienValidator.validate(data)
        return self.repo.save(data)
