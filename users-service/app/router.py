from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas
from .service import create_user, list_users, get_user
from .deps import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=schemas.Usuario)
def create_user_endpoint(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=list[schemas.Usuario])
def list_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)


@router.get("/{user_id}", response_model=schemas.Usuario)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)
