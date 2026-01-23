class NhanVienRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, ma_nv, ten_nv, vai_tro, trang_thai, password_hash):
        sql = """
        INSERT INTO nhan_vien
        (ma_nv, ten_nv, vai_tro, trang_thai, password_hash)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (ma_nv, ten_nv, vai_tro, trang_thai, password_hash))
        self.conn.commit()
