from master.validators.san_pham_validator import SanPhamValidator


class SanPhamService:
    def __init__(self, repo):
        self.repo = repo

    def tao_moi(self, data):
        SanPhamValidator.validate(data)
        return self.repo.save(data)
