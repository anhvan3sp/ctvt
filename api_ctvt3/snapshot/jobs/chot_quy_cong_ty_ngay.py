from snapshot.builders.quy_cong_ty_builder import QuyCongTyBuilder


class ChotQuyCongTyNgayJob:
    def __init__(self, journal_repo, snapshot_repo):
        self.journal_repo = journal_repo
        self.snapshot_repo = snapshot_repo

    def run(self, ngay):
        so_du = self.journal_repo.tinh_quy_cong_ty(ngay)
        snapshot = QuyCongTyBuilder.build(ngay, so_du)
        self.snapshot_repo.save(snapshot)
