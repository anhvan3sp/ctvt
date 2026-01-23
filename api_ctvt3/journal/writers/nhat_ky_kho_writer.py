class NhatKyKhoWriter:
    def __init__(self, repo):
        self.repo = repo

    def write(self, danh_sach_nhat_ky):
        for nk in danh_sach_nhat_ky:
            self.repo.save(nk)
