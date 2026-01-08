from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_hoa_don_nhap, create_hoa_don_nhap
from schemas import HoaDonNhapCreate, HoaDonNhapRead

router = APIRouter(
    prefix="/hoa_don_nhap",   # GIỮ NGUYÊN
    tags=["hoa_don_nhap"]
)


@router.get("/", response_model=List[HoaDonNhapRead])
def read_hoa_don_nhap(db: Session = Depends(get_db)):
    """
    Lấy danh sách hóa đơn nhập.
    Trigger DB đã xử lý tồn kho, công nợ, VAT.
    """
    return get_hoa_don_nhap(db)


@router.post("/", response_model=HoaDonNhapRead)
def add_hoa_don_nhap(data: HoaDonNhapCreate, db: Session = Depends(get_db)):
    """
    Thêm hóa đơn nhập.
    Toàn bộ nghiệp vụ nằm trong trigger DB.
    """
    return create_hoa_don_nhap(db, data)
