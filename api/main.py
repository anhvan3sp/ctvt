from fastapi import FastAPI

from routers import (
    auth,
    products,
    kho_hang,
    nhan_vien,
    khach_hang,
    nha_cung_cap,
    hoa_don_ban,
    hoa_don_nhap,
    thu_chi,
    dashboard,
    don_dat_hang_ban,
    don_dat_hang_nhap,
)

# =====================================================
# CREATE FASTAPI APP
# =====================================================
app = FastAPI(
    title="API ct_vt",
    version="2.0"
)

# =====================================================
# INCLUDE ROUTERS
# =====================================================

# ✅ Auth: KHÔNG gắn prefix ở đây
# vì router auth.py ĐÃ có prefix="/auth"
app.include_router(auth.router)

# Danh mục
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(kho_hang.router, prefix="/kho-hang", tags=["Kho hàng"])
app.include_router(nhan_vien.router, prefix="/nhan-vien", tags=["Nhân viên"])
app.include_router(khach_hang.router, prefix="/khach-hang", tags=["Khách hàng"])
app.include_router(nha_cung_cap.router, prefix="/nha-cung-cap", tags=["Nhà cung cấp"])

# Đơn đặt
# ⚠️ router ĐÃ có prefix bên trong → KHÔNG gắn thêm
app.include_router(don_dat_hang_ban.router)
app.include_router(don_dat_hang_nhap.router)

# Hóa đơn
app.include_router(hoa_don_ban.router, prefix="/hoa-don-ban", tags=["Hóa đơn bán"])
app.include_router(hoa_don_nhap.router, prefix="/hoa-don-nhap", tags=["Hóa đơn nhập"])

# Thu chi & dashboard
app.include_router(thu_chi.router, prefix="/thu-chi", tags=["Thu chi"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

# =====================================================
# ROOT CHECK
# =====================================================
@app.get("/")
def root():
    return {"message": "API ct_vt is running"}

