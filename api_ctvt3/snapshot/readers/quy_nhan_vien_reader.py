class QuyNhanVienReader:
    def __init__(self, repo):
        self.repo = repo

    def lay_quy_nhan_vien(self, ngay):
        return self.repo.get_quy_nhan_vien(ngay)
