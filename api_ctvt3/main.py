# main.py
from config import APP_NAME, APP_ENV, DEBUG


def bootstrap():
    """
    Khởi tạo hệ thống:
    - load config
    - init DB (infra layer)
    - init system services
    - init modules
    """
    print(f"Starting {APP_NAME}")
    print(f"Environment: {APP_ENV}")
    print(f"Debug: {DEBUG}")

    # NOTE:
    # - DB connection pool khởi tạo ở đây (infra)
    # - Migration / check schema nếu cần
    # - Wiring dependency (DI) nếu dùng

    print("System bootstrap completed")


def start_api():
    """
    Start API server
    (FastAPI / Flask sẽ được gắn vào đây sau)
    """
    print("API is ready to receive requests")


if __name__ == "__main__":
    bootstrap()
    start_api()
