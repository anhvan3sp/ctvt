from functools import wraps


def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            # commit DB ở tầng infra
            return result
        except Exception:
            # rollback DB ở tầng infra
            raise
    return wrapper
