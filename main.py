from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

# Configuração do banco de dados (Exemplo com SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Criação da engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa do SQLAlchemy
Base = declarative_base()

# Definição do modelo SQLAlchemy
class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    ano_lancamento = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criação do aplicativo FastAPI
app = FastAPI()

# Pydantic model para validação de entrada e saída
class JogoCreate(BaseModel):
    nome: str
    ano_lancamento: int

class JogoOut(JogoCreate):
    id: int

    class Config:
        orm_mode = True

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Jogos!"}

# Rota para listar todos os jogos
@app.get("/jogos", response_model=List[JogoOut])
def get_jogos(db: Session = Depends(get_db)):
    jogos = db.query(Jogo).all()
    return jogos

# Rota para criar um novo jogo
@app.post("/jogos", response_model=JogoOut)
def create_jogo(jogo: JogoCreate, db: Session = Depends(get_db)):
    db_jogo = Jogo(nome=jogo.nome, ano_lancamento=jogo.ano_lancamento)
    db.add(db_jogo)
    db.commit()
    db.refresh(db_jogo)
    return db_jogo

# Rota para obter um jogo específico pelo ID
@app.get("/jogos/{jogo_id}", response_model=JogoOut)
def get_jogo(jogo_id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == jogo_id).first()
    if jogo is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return jogo

