class SanPhamValidator:
    @staticmethod
    def validate(data):
        if not data.get("ten"):
            raise Exception("Thiếu tên sản phẩm")
