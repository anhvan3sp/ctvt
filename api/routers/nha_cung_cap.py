from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_nha_cung_cap, create_nha_cung_cap
from schemas import NhaCungCapCreate, NhaCungCapRead

router = APIRouter(
    prefix="/nha_cung_cap",   # GIỮ NGUYÊN
    tags=["nha_cung_cap"]
)


@router.get("/", response_model=List[NhaCungCapRead])
def read_nha_cung_cap(db: Session = Depends(get_db)):
    return get_nha_cung_cap(db)


@router.post("/", response_model=NhaCungCapRead)
def add_nha_cung_cap(data: NhaCungCapCreate, db: Session = Depends(get_db)):
    return create_nha_cung_cap(db, data)
