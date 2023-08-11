import sys
sys.path.append('.')

from sqlalchemy import Boolean, Column, Float, Integer, String
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    preco = Column(Float)
    detalhes = Column(String)
    disponivel = Column(Boolean)