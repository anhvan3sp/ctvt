from master.validators.kho_hang_validator import KhoHangValidator


class KhoHangService:
    def __init__(self, repo):
        self.repo = repo

    def tao_moi(self, data):
        KhoHangValidator.validate(data)
        return self.repo.save(data)
