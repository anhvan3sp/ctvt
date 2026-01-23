class SanPhamRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, ma_sp, ten_sp, loai_san_pham, don_vi_tinh, dung_tich_kg):
        sql = """
        INSERT INTO san_pham
        (ma_sp, ten_sp, loai_san_pham, don_vi_tinh, dung_tich_kg)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (ma_sp, ten_sp, loai_san_pham, don_vi_tinh, dung_tich_kg))
        self.conn.commit()
