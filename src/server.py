import sys
sys.path.append('.')

from typing import List
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto

criar_bd()
 
app = FastAPI()

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=list[Produto]) #error here!
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    print(produtos)
    return produtos
