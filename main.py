from typing import Union
from fastapi import FastAPI
from GeradorDeSenha import geradorDeSenha
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/geradorDeSenha")
def reed_geradorDeSenha(tamanho: int, quantidade: int):
    return geradorDeSenha([quantidade, tamanho])

