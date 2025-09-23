from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Jogo(Base):
    __tablename__ = 'jogos'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    ano_lancamento = Column(Integer)
