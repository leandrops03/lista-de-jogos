from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Jogador
from sqlalchemy.orm import Session

app = FastAPI()

# Endpoint para criar um novo jogador
@app.post("/jogador/")
def criar_jogador(nome: str, jogo: str, db: Session = Depends(get_db)):
    # Criando um novo jogador
    jogador = Jogador(nome=nome, jogo=jogo)
    db.add(jogador)
    db.commit()
    db.refresh(jogador)
    return jogador

# Endpoint para listar todos os jogadores
@app.get("/jogadores/")
def listar_jogadores(db: Session = Depends(get_db)):
    jogadores = db.query(Jogador).all()
    return jogadores

# Endpoint para pegar um jogador pelo id
@app.get("/jogador/{jogador_id}")
def obter_jogador(jogador_id: int, db: Session = Depends(get_db)):
    jogador = db.query(Jogador).filter(Jogador.id == jogador_id).first()
    if jogador is None:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogador
