from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import (
    get_khach_hang,
    create_khach_hang,
    search_khach_hang,
)
from schemas import KhachHangCreate, KhachHangRead

router = APIRouter(
    prefix="/khach-hang",     # GIỮ NGUYÊN
    tags=["KhachHang"]
)

# =====================================================
# GET: LẤY TOÀN BỘ KHÁCH HÀNG
# =====================================================
@router.get("/", response_model=List[KhachHangRead])
def get_all_khach_hang(db: Session = Depends(get_db)):
    return get_khach_hang(db)


# =====================================================
# GET: TÌM KHÁCH HÀNG (AUTOCOMPLETE)
# =====================================================
@router.get("/search", response_model=List[KhachHangRead])
def search_khach_hang_api(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    return search_khach_hang(db, keyword)


# =====================================================
# POST: THÊM KHÁCH HÀNG
# =====================================================
@router.post("/", response_model=KhachHangRead)
def create_khach_hang_api(
    kh: KhachHangCreate,
    db: Session = Depends(get_db)
):
    return create_khach_hang(db, kh)
