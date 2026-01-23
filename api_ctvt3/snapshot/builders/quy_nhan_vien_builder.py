from snapshot.entities.quy_nhan_vien_chot_ngay import QuyNhanVienChotNgay


class QuyNhanVienBuilder:
    @staticmethod
    def build(ngay, du_lieu):
        return [
            QuyNhanVienChotNgay(
                ngay=ngay,
                nhan_vien_id=d.nhan_vien_id,
                so_du=d.so_du,
            )
            for d in du_lieu
        ]
