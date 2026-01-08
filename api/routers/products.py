from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_san_pham, create_san_pham
from schemas import SanPhamCreate, SanPhamRead

router = APIRouter(
    prefix="/products",     # GIỮ NGUYÊN để không ảnh hưởng app cũ
    tags=["Products"]
)


@router.get("/", response_model=List[SanPhamRead])
def read_products(db: Session = Depends(get_db)):
    return get_san_pham(db)


@router.post("/", response_model=SanPhamRead)
def add_product(data: SanPhamCreate, db: Session = Depends(get_db)):
    return create_san_pham(db, data)
