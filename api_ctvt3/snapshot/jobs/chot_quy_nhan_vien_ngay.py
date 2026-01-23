from snapshot.builders.quy_nhan_vien_builder import QuyNhanVienBuilder


class ChotQuyNhanVienNgayJob:
    def __init__(self, journal_repo, snapshot_repo):
        self.journal_repo = journal_repo
        self.snapshot_repo = snapshot_repo

    def run(self, ngay):
        du_lieu = self.journal_repo.tinh_quy_nhan_vien(ngay)
        danh_sach = QuyNhanVienBuilder.build(ngay, du_lieu)
        for dong in danh_sach:
            self.snapshot_repo.save(dong)
