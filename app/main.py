from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import engine, Base
from .routers import alunos, agenda, professores, turmas, disciplinas, matriculas


# cria tabelas caso não existam
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Base Agenda")


# registrar routers
app.include_router(alunos.router)
app.include_router(agenda.router)
app.include_router(professores.router)
app.include_router(turmas.router)
app.include_router(disciplinas.router)
app.include_router(matriculas.router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def homepage(request: Request):
    """Renderiza a página inicial (links para Swagger e Redoc)."""
    return templates.TemplateResponse("index.html", {"request": request})
