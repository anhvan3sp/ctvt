from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime
from pydantic import BaseModel

from database import get_db
from models import DonDatHangBan, HoaDonBan
from auth_utils import get_current_user

router = APIRouter(
    prefix="/don-dat-ban",
    tags=["Đơn đặt bán"]
)

# =====================================================
# SCHEMA TAO DON DAT BAN
# =====================================================
class DonDatBanCreate(BaseModel):
    ma_kh: str
    tong_tien_du_kien: float
    ghi_chu: str | None = None


# =====================================================
# TAO DON DAT BAN
# =====================================================
@router.post("")
def tao_don_dat_ban(
    data: DonDatBanCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    ma_don = f"DDB-{int(datetime.now().timestamp())}"

    don = DonDatHangBan(
        ma_don=ma_don,
        ma_kh=data.ma_kh,
        ngay_dat=date.today(),
        tong_tien_du_kien=data.tong_tien_du_kien,
        trang_thai="dat_hang",
        ghi_chu=data.ghi_chu
    )

    db.add(don)
    db.commit()
    db.refresh(don)

    return {
        "message": "Da tao don dat ban",
        "don_dat_id": don.id,
        "ma_don": don.ma_don
    }


# =====================================================
# TAO HOA DON BAN TU DON DAT
# =====================================================
@router.post("/{don_id}/tao-hoa-don")
def tao_hoa_don_ban_tu_don(
    don_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    don = db.query(DonDatHangBan).filter(
        DonDatHangBan.id == don_id,
        DonDatHangBan.trang_thai == "dat_hang"
    ).first()

    if not don:
        raise HTTPException(
            status_code=404,
            detail="Don dat khong ton tai hoac da duoc xu ly"
        )

    hoa_don = HoaDonBan(
        ngay=date.today(),
        ma_kh=don.ma_kh,
        ghi_chu=f"Sinh tu don dat {don.ma_don}"
    )

    db.add(hoa_don)
    db.flush()  # lay hoa_don.id

    don.trang_thai = "da_giao"

    db.commit()

    return {
        "message": "Da tao hoa don ban",
        "hoa_don_id": hoa_don.id
    }

