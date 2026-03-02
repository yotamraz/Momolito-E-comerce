from sqlalchemy.orm import Session
from . import models, schemas


def get_all(db: Session):
    return db.query(models.Usuario).all()


def get_by_id(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()


def get_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()


def create(db: Session, user: schemas.UsuarioCreate):
    db_user = models.Usuario(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
