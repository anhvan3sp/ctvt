class GasDuReader:
    def __init__(self, repo):
        self.repo = repo

    def lay_gas_du(self, ngay):
        return self.repo.get_gas_du(ngay)
