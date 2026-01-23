from master.validators.nha_cung_cap_validator import NhaCungCapValidator


class NhaCungCapService:
    def __init__(self, repo):
        self.repo = repo

    def tao_moi(self, data):
        NhaCungCapValidator.validate(data)
        return self.repo.save(data)
