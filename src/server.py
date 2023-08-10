import sys
sys.path.append('.')

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto

criar_bd()
 
app = FastAPI()

@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos():
    return {'Mensagem': 'Lsiatgem de produtos'}
