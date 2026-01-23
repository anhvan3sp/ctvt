class KhoHangRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, ma_kho, ten_kho):
        sql = """
        INSERT INTO kho_hang (ma_kho, ten_kho)
        VALUES (%s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (ma_kho, ten_kho))
        self.conn.commit()
