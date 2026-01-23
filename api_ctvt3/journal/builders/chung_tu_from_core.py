from journal.entities.log_chung_tu import LogChungTu


class ChungTuFromCore:
    @staticmethod
    def build(chung_tu_id, loai_su_kien, mo_ta, thoi_diem):
        return LogChungTu(
            chung_tu_id=chung_tu_id,
            loai_su_kien=loai_su_kien,
            mo_ta=mo_ta,
            thoi_diem=thoi_diem,
        )
