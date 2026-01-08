from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from pydantic import BaseModel

from database import get_db
from models import ThuChi
from auth_utils import get_current_user

router = APIRouter(
    prefix="/thu-chi",
    tags=["Thu chi"]
)

# =====================================================
# SCHEMA THU / CHI (KHỚP ct_vt_schema.sql)
# =====================================================
class ThuChiCreate(BaseModel):
    ngay: date | None = None
    so_tien: float

    hinh_thuc: str      # tien_mat | chuyen_khoan
    loai_gd: str        # thu | chi

    danh_muc: str | None = None
    noi_dung: str | None = None


# =====================================================
# TẠO PHIẾU THU / CHI
# =====================================================
@router.post("")
def tao_phieu_thu_chi(
    data: ThuChiCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    - API chỉ ghi nhận thu/chi
    - Không gắn ref nghiệp vụ ở đây
    - Công nợ / quỹ / liên kết xử lý bằng trigger hoặc logic DB
    """

    phieu = ThuChi(
        ngay=data.ngay or date.today(),
        ma_nv=current_user["ma_nv"],
        so_tien=data.so_tien,
        hinh_thuc=data.hinh_thuc,
        loai_gd=data.loai_gd,
        danh_muc=data.danh_muc,
        noi_dung=data.noi_dung
    )

    db.add(phieu)
    db.commit()
    db.refresh(phieu)

    return {
        "message": "Da tao phieu thu chi",
        "thu_chi_id": phieu.id
    }

