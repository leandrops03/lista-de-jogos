from sqlalchemy import Column, Integer, String
from .database import Base

# Definindo o modelo Jogador
class Jogador(Base):
    __tablename__ = "jogadores"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    jogo = Column(String)
