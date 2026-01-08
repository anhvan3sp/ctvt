from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_nhan_vien, create_nhan_vien
from schemas import NhanVienCreate, NhanVienRead

router = APIRouter(
    prefix="/nhan_vien",   # GIỮ NGUYÊN
    tags=["nhan_vien"]
)


@router.get("/", response_model=List[NhanVienRead])
def read_nhan_vien(db: Session = Depends(get_db)):
    return get_nhan_vien(db)


@router.post("/", response_model=NhanVienRead)
def add_nhan_vien(data: NhanVienCreate, db: Session = Depends(get_db)):
    return create_nhan_vien(db, data)
