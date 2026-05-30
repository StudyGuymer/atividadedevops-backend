from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1 import users
from app.api.v1 import favorites

# Cria as tabelas no banco na inicialização
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Usuários", version="1.0.0")

app.include_router(users.router, prefix="/api/v1")
app.include_router(favorites.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "ok"}