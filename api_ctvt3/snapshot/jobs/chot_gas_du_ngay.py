from snapshot.builders.gas_du_builder import GasDuBuilder


class ChotGasDuNgayJob:
    def __init__(self, journal_repo, snapshot_repo):
        self.journal_repo = journal_repo
        self.snapshot_repo = snapshot_repo

    def run(self, ngay):
        du_lieu = self.journal_repo.lay_gas_du(ngay)
        danh_sach = GasDuBuilder.build(ngay, du_lieu)
        for dong in danh_sach:
            self.snapshot_repo.save(dong)
