from common.exceptions.validation_exception import ValidationException


class BaseValidator:
    def error(self, message: str):
        raise ValidationException(message)
