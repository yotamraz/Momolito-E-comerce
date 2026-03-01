from pydantic import BaseModel, ConfigDict, Field


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=120)
    email: str


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
