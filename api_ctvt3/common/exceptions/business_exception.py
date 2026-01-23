from common.exceptions.base_exception import BaseExceptionCTVT


class BusinessException(BaseExceptionCTVT):
    def __init__(self, message: str):
        super().__init__(message, code="BUSINESS_ERROR")
