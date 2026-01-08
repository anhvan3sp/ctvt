from sqlalchemy.orm import Session
from sqlalchemy import text


def get_doanh_thu_ngay(db: Session):
    return db.execute(text("SELECT * FROM v_doanh_thu_ngay")).mappings().all()


def get_doanh_thu_thang(db: Session):
    return db.execute(text("SELECT * FROM v_doanh_thu_thang")).mappings().all()


def get_cong_no_khach(db: Session):
    return db.execute(text("SELECT * FROM v_cong_no_khach")).mappings().all()


def get_ton_kho(db: Session):
    return db.execute(text("SELECT * FROM v_ton_kho_thuc")).mappings().all()
