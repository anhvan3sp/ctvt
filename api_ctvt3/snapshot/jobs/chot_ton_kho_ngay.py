from snapshot.builders.ton_kho_builder import TonKhoBuilder


class ChotTonKhoNgayJob:
    def __init__(self, journal_repo, snapshot_repo):
        self.journal_repo = journal_repo
        self.snapshot_repo = snapshot_repo

    def run(self, ngay):
        du_lieu = self.journal_repo.lay_ton_kho(ngay)
        danh_sach = TonKhoBuilder.build(ngay, du_lieu)
        for dong in danh_sach:
            self.snapshot_repo.save(dong)
