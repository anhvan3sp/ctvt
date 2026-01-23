from snapshot.entities.gas_du_chot_ngay import GasDuChotNgay


class GasDuBuilder:
    @staticmethod
    def build(ngay, du_lieu_journal):
        return [
            GasDuChotNgay(
                ngay=ngay,
                san_pham_id=d.san_pham_id,
                so_luong_du=d.so_luong_du,
            )
            for d in du_lieu_journal
        ]
