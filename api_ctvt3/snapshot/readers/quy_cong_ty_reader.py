class QuyCongTyReader:
    def __init__(self, repo):
        self.repo = repo

    def lay_quy(self, ngay):
        return self.repo.get_quy_cong_ty(ngay)
