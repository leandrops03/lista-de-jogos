from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class Jogo(Base):
    _tablename_ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    genero = Column(String, nullable=True)
    finalizado = Column(Boolean, default=False)
    data_adicao = Column(DateTime, default=datetime.utcnow)
