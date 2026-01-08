from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth_utils import get_current_user
from crud_dashboard import (
    get_doanh_thu_ngay,
    get_doanh_thu_thang,
    get_cong_no_khach,
    get_ton_kho,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/doanh-thu-ngay")
def dashboard_doanh_thu_ngay(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_doanh_thu_ngay(db)


@router.get("/doanh-thu-thang")
def dashboard_doanh_thu_thang(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_doanh_thu_thang(db)


@router.get("/cong-no-khach")
def dashboard_cong_no_khach(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_cong_no_khach(db)


@router.get("/ton-kho")
def dashboard_ton_kho(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_ton_kho(db)
