class TonKhoReader:
    def __init__(self, repo):
        self.repo = repo

    def lay_ton_kho(self, ngay):
        return self.repo.get_ton_kho(ngay)
