class KhachHangRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, ma_kh, ten_cua_hang, dia_chi, so_dien_thoai, ma_so_thue, ghi_chu):
        sql = """
        INSERT INTO khach_hang
        (ma_kh, ten_cua_hang, dia_chi, so_dien_thoai, ma_so_thue, ghi_chu)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (ma_kh, ten_cua_hang, dia_chi, so_dien_thoai, ma_so_thue, ghi_chu))
        self.conn.commit()
