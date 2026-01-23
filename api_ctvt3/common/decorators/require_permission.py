from functools import wraps
from common.exceptions.permission_exception import PermissionException


def require_permission(permission_code: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            permissions = kwargs.get("permissions", [])
            if permission_code not in permissions:
                raise PermissionException()
            return func(*args, **kwargs)
        return wrapper
    return decorator
