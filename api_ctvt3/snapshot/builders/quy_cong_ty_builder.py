from snapshot.entities.quy_cong_ty_chot_ngay import QuyCongTyChotNgay


class QuyCongTyBuilder:
    @staticmethod
    def build(ngay, so_du):
        return QuyCongTyChotNgay(
            ngay=ngay,
            so_du=so_du,
        )
