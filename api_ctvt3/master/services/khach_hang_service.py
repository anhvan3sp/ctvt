from master.validators.khach_hang_validator import KhachHangValidator


class KhachHangService:
    def __init__(self, repo):
        self.repo = repo

    def tao_moi(self, data):
        KhachHangValidator.validate(data)
        return self.repo.save(data)
