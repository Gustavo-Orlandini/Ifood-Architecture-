from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = False
    endereco: str   
    observacoes: Optional[str] = 'Sem observações' 