class NhaCungCapValidator:
    @staticmethod
    def validate(data):
        if not data.get("ten"):
            raise Exception("Thiếu tên nhà cung cấp")
