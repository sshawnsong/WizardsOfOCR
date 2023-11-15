from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from .models import Parcels

DB_URL = 'postgresql://postgres:0404@localhost:5432/wizardsofocr'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_parcel(db: Session, name: str, is_active: bool = False):
    db_parcel = Parcels(name=name, is_active=is_active)
    db.add(db_parcel)
    db.commit()
    db.refresh(db_parcel)
    return db_parcel


def read_parcel(db: Session, name: str):
    return db.query(Parcels).filter(Parcels.name == name).first()


def read_parcels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Parcels).offset(skip).limit(limit).all()


def update_parcel(db: Session, parcel_id: int, new_status: bool):
    db_parcel = db.query(Parcels).filter(Parcels.id == parcel_id).first()
    if db_parcel:
        db_parcel.is_active = new_status
        db.commit()
        db.refresh(db_parcel)
        return db_parcel
    return None
