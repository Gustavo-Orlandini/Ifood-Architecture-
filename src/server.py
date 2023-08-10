from fastapi import FastAPI

app = FastAPI()

@app.get('/produtos')
def listar_produtos():
    return {'Mensagem': 'Lsiatgem de produtos'}
