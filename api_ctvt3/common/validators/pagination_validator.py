from common.validators.base_validator import BaseValidator
from common.constants.pagination_constants import MAX_PAGE_SIZE


class PaginationValidator(BaseValidator):
    def validate(self, page: int, size: int):
        if page < 1:
            self.error("Page phải >= 1")
        if size < 1 or size > MAX_PAGE_SIZE:
            self.error("Page size không hợp lệ")
