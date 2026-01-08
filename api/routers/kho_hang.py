from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_kho_hang, create_kho_hang
from schemas import KhoHangCreate, KhoHangRead

router = APIRouter(
    prefix="/kho_hang",   # GIỮ NGUYÊN
    tags=["kho_hang"]
)


@router.get("/", response_model=List[KhoHangRead])
def read_kho_hang(db: Session = Depends(get_db)):
    return get_kho_hang(db)


@router.post("/", response_model=KhoHangRead)
def add_kho_hang(data: KhoHangCreate, db: Session = Depends(get_db)):
    return create_kho_hang(db, data)
