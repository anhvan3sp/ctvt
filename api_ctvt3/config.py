# config.py
import os

# =========================
# APP
# =========================
APP_NAME = "CTVT3"
APP_ENV = os.getenv("APP_ENV", "local")  # local | dev | prod
DEBUG = APP_ENV != "prod"

# =========================
# DATABASE
# =========================
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "ctvt3")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)

# =========================
# AUTH / SESSION
# =========================
SESSION_EXPIRE_HOURS = 12
TOKEN_HEADER = "Authorization"

# =========================
# PAGINATION
# =========================
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# =========================
# TIMEZONE
# =========================
TIMEZONE = "Asia/Ho_Chi_Minh"

# =========================
# AUDIT
# =========================
ENABLE_AUDIT_LOG = True
