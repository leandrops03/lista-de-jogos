from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Biblioteca de jogos")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/jogos/", response_model=schemas.Jogo)
def criar_jogo(jogo: schemas.JogoCreate, db: Session = Depends(get_db)):
    return crud.criar_jogo(db, jogo)

@app.get("/jogos/", response_model=list[schemas.Jogo])
def listar_jogos(db: Session = Depends(get_db)):
    return crud.listar_jogos(db)

@app.put("/jogos/{jogo_id}", response_model=schemas.Jogo)
def atualizar_jogo(jogo_id: int, jogo: schemas.JogoUpdate, db: Session = Depends(get_db)):
    db_jogo = crud.atualizar_jogo(db, jogo_id, jogo)
    if not db_jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db_jogo

@app.delete("/jogos/{jogo_id}")
def deletar_jogo(jogo_id: int, db: Session = Depends(get_db)):
    db_jogo = crud.excluir_jogo(db, jogo_id)
    if not db_jogo:
        raise HTTPException(status_code=404, detail="não encontrado")
    return {"mensagem": "Jogo removido}
