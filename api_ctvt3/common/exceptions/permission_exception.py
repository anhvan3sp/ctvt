from common.exceptions.base_exception import BaseExceptionCTVT


class PermissionException(BaseExceptionCTVT):
    def __init__(self, message: str = "Không có quyền thao tác"):
        super().__init__(message, code="PERMISSION_DENIED")
