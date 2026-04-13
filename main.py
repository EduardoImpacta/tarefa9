from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "ok"}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}