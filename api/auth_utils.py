from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# =====================================================
# CONFIG – PHẢI KHỚP auth.py
# =====================================================
SECRET_KEY = "ctvt_secret_key_doi_sau"   # sau này đổi
ALGORITHM = "HS256"

# OAuth2 – FastAPI dùng để đọc header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# =====================================================
# GIẢI MÃ TOKEN – LẤY THÔNG TIN USER
# =====================================================
def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    - Kiểm tra token
    - Giải mã JWT
    - Trả về dict: username, ma_nv, role
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")
        ma_nv: str = payload.get("ma_nv")
        role: str = payload.get("role")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token không hợp lệ"
            )

        return {
            "username": username,
            "ma_nv": ma_nv,
            "role": role
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ hoặc đã hết hạn"
        )


# =====================================================
# KIỂM TRA PHÂN QUYỀN
# =====================================================
def require_role(allowed_roles: list[str]):
    """
    Dùng để chặn API theo role
    Ví dụ: require_role(["admin"])
    """
    def checker(current_user = Depends(get_current_user)):
        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Không đủ quyền truy cập"
            )
        return current_user

    return checker
