from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime
from pydantic import BaseModel

from database import get_db
from models import DonDatHangNhap, HoaDonNhap
from auth_utils import get_current_user

router = APIRouter(
    prefix="/don-dat-nhap",
    tags=["Đơn đặt nhập"]
)

# =====================================================
# SCHEMA TAO DON DAT NHAP
# =====================================================
class DonDatNhapCreate(BaseModel):
    ma_ncc: str
    tong_tien_du_kien: float
    ghi_chu: str | None = None


# =====================================================
# TAO DON DAT NHAP (NHA CUNG CAP)
# =====================================================
@router.post("")
def tao_don_dat_nhap(
    data: DonDatNhapCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    ma_don = f"DDN-{int(datetime.now().timestamp())}"

    don = DonDatHangNhap(
        ma_don=ma_don,
        ma_ncc=data.ma_ncc,
        ngay_dat=date.today(),
        tong_tien_du_kien=data.tong_tien_du_kien,
        trang_thai="dat_hang",
        ghi_chu=data.ghi_chu
    )

    db.add(don)
    db.commit()
    db.refresh(don)

    return {
        "message": "Da tao don dat nhap",
        "don_dat_id": don.id,
        "ma_don": don.ma_don
    }


# =====================================================
# TAO HOA DON NHAP TU DON DAT NHAP
# =====================================================
@router.post("/{don_id}/tao-hoa-don")
def tao_hoa_don_nhap_tu_don(
    don_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    don = db.query(DonDatHangNhap).filter(
        DonDatHangNhap.id == don_id,
        DonDatHangNhap.trang_thai == "dat_hang"
    ).first()

    if not don:
        raise HTTPException(
            status_code=404,
            detail="Don dat nhap khong ton tai hoac da duoc xu ly"
        )

    hoa_don = HoaDonNhap(
        ngay=date.today(),
        ma_ncc=don.ma_ncc,
        ghi_chu=f"Sinh tu don dat nhap {don.ma_don}"
    )

    db.add(hoa_don)
    db.flush()  # lay hoa_don.id

    don.trang_thai = "da_nhap"

    db.commit()

    return {
        "message": "Da tao hoa don nhap",
        "hoa_don_id": hoa_don.id
    }

