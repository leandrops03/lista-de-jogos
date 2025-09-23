from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados (aqui estamos usando SQLite para simplicidade)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Criação da engine para conectar ao banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Criando uma sessão que será usada nas operações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base que será usada para criar os modelos (tabelas)
Base = declarative_base()

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
