from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import schemas
from .repository import get_all, get_by_id, get_by_email, create


def create_user(db: Session, user: schemas.UsuarioCreate):
    existing = get_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado.")
    return create(db, user)


def list_users(db: Session):
    return get_all(db)


def get_user(db: Session, user_id: int):
    user = get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user
