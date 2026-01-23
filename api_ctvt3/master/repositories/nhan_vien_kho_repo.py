class NhanVienKhoRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, ma_nv, ma_kho):
        sql = """
        INSERT INTO nhan_vien_kho (ma_nv, ma_kho)
        VALUES (%s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (ma_nv, ma_kho))
        self.conn.commit()
