class NhanVienValidator:
    @staticmethod
    def validate(data):
        if not data.get("ten"):
            raise Exception("Thiếu tên nhân viên")
