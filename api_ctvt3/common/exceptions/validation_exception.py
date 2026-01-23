from common.exceptions.base_exception import BaseExceptionCTVT


class ValidationException(BaseExceptionCTVT):
    def __init__(self, message: str):
        super().__init__(message, code="VALIDATION_ERROR")
