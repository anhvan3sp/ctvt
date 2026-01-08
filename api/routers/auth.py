from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from database import get_db
from schemas import LoginResponse

# =====================================================
# CONFIG
# =====================================================
SECRET_KEY = "ctvt_secret_key_2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 ngày

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# =====================================================
# UTILS
# =====================================================
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# =====================================================
# API: LOGIN (OAuth2 CHUẨN)
# =====================================================
@router.post("/login", response_model=LoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    sql = text("""
        SELECT
            username,
            password_hash,
            ma_nv,
            role
        FROM nguoi_dung
        WHERE username = :username
        LIMIT 1
    """)

    user = db.execute(
        sql,
        {"username": form_data.username}
    ).mappings().first()

    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai tài khoản hoặc mật khẩu"
        )

    access_token = create_access_token(
        data={
            "sub": user["username"],
            "ma_nv": user["ma_nv"],
            "role": user["role"]
        },
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "ma_nv": user["ma_nv"],
        "role": user["role"]
    }

