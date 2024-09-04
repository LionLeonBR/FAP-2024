from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# tabela usuario

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=db)

usuario = Usuario(nome="Roberto", email="leo@gmail.com", senha="1234")
session.add(usuario)
session.commit()
usuario_roberto = session.query(Usuario).filter_by(nome="Roberto").first()
print(usuario_roberto.email)