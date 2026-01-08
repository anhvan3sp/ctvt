from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import get_hoa_don_ban, create_hoa_don_ban
from schemas import HoaDonBanCreate, HoaDonBanRead
from auth_utils import get_current_user

router = APIRouter(
    prefix="/hoa_don_ban",
    tags=["hoa_don_ban"]
)


@router.get("/", response_model=List[HoaDonBanRead])
def read_hoa_don_ban(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Lấy danh sách hóa đơn bán.
    Yêu cầu đăng nhập hợp lệ.
    """
    return get_hoa_don_ban(db)


@router.post("/", response_model=HoaDonBanRead)
def add_hoa_don_ban(
    data: HoaDonBanCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Thêm hóa đơn bán.
    - ma_nv lấy từ token
    - Trigger DB xử lý tồn kho, vỏ, công nợ
    """
    data.ma_nv = current_user["ma_nv"]
    return create_hoa_don_ban(db, data)
