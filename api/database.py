from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =====================================================
# Database configuration for ct_vt
# =====================================================

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://api_user:123456789abC%40@localhost/ct_vt"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,          # bật log SQL khi dev
    pool_pre_ping=True  # tránh lỗi mất kết nối MySQL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# =====================================================
# Dependency dùng cho FastAPI
# =====================================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
