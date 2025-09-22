from pydantic import BaseModel
from datetime import datetime

class JogoBase(BaseModel):
    titulo: str
    genero: str | None = None

class JogoCreate(JogoBase):
    pass

class JogoUpdate(BaseModel):
    titulo: str | None = None
    genero: str | None = None
    finalizado: bool | None = None

class Jogo(JogoBase):
    id: int
    finalizado: bool
    data_adicao: datetime

    class Config:
        orm_mode = True
