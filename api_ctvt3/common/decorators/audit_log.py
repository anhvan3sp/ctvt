from functools import wraps


def audit_log(action: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # ghi audit ở tầng service
            return func(*args, **kwargs)
        return wrapper
    return decorator
