from common.validators.base_validator import BaseValidator
from common.utils.string_utils import is_empty


class RequestValidator(BaseValidator):
    def require(self, value, field_name: str):
        if value is None or (isinstance(value, str) and is_empty(value)):
            self.error(f"Thiếu dữ liệu: {field_name}")
