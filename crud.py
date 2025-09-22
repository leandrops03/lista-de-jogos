from sqlalchemy.orm import Session
import models, schemas

def listar_jogos(db: Session):
    return db.query(models.Jogo).order_by(models.Jogo.data_adicao.desc()).all()

def criar_jogo(db: Session, jogo: schemas.JogoCreate):
    db_jogo = models.Jogo(titulo=jogo.titulo, genero=jogo.genero)
    db.add(db_jogo)
    db.commit()
    db.refresh(db_jogo)
    return db_jogo

def atualizar_jogo(db: Session, jogo_id: int, jogo: schemas.JogoUpdate):
    db_jogo = db.query(models.Jogo).filter(models.Jogo.id == jogo_id).first()
    if db_jogo:
        if jogo.titulo is not None:
            db_jogo.titulo = jogo.titulo
        if jogo.genero is not None:
            db_jogo.genero = jogo.genero
        if jogo.finalizado is not None:
            db_jogo.finalizado = jogo.finalizado
        db.commit()
        db.refresh(db_jogo)
    return db_jogo

def deletar_jogo(db: Session, jogo_id: int):
    db_jogo = db.query(models.Jogo).filter(models.Jogo.id == jogo_id).first()
    if db_jogo:
        db.delete(db_jogo)
        db.commit()
    return db_jogo
