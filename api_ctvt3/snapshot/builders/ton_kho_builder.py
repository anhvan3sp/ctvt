from snapshot.entities.ton_kho_chot_ngay import TonKhoChotNgay


class TonKhoBuilder:
    @staticmethod
    def build(ngay, du_lieu_journal):
        ket_qua = []
        for dong in du_lieu_journal:
            ket_qua.append(
                TonKhoChotNgay(
                    ngay=ngay,
                    kho_id=dong.kho_id,
                    san_pham_id=dong.san_pham_id,
                    so_luong_ton=dong.so_luong_ton,
                )
            )
        return ket_qua
