from sqlalchemy import Boolean, Column, Float, Interger, String
from infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Interger, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(Float)
    disponivel = Column(Boolean)