from sqlalchemy import Boolean, Column, Float, Interger, String

class Produto():
    id = Column(Interger, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(Float)
    disponivel = Column(Boolean)