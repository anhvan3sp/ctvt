from fastapi import APIRouter, HTTPException
from core.database import get_db
from core.security import verify_password, create_token

router = APIRouter()

@router.post("/login")
def login(ma_nv: str, password: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT ma_nv, ten_nv, vai_tro, password_hash "
        "FROM nhan_vien WHERE ma_nv = %s",
        (ma_nv,)
    )
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Sai ma_nv")

    if not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Sai mat khau")

    token = create_token({
        "ma_nv": user["ma_nv"],
        "vai_tro": user["vai_tro"]
    })

    return {
        "access_token": token,
        "user": {
            "ma_nv": user["ma_nv"],
            "ten_nv": user["ten_nv"],
            "vai_tro": user["vai_tro"]
        }
    }
