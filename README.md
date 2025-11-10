
# API Base Agenda

Uma API simples para gerenciar alunos e uma agenda escolar. A aplicação fornece endpoints REST para criar, listar, atualizar e deletar alunos e entradas de agenda. É construída com FastAPI, SQLAlchemy e Pydantic.

## Tech stack

- Python 3.8+ — linguagem usada para implementar a API.
- FastAPI — framework web para criar APIs rápidas com documentação automática.
- SQLAlchemy — ORM/SQL toolkit para acessar e modelar o banco de dados.
- Pydantic — validação e serialização de dados (schemas).
- Jinja2 — motor de templates para páginas HTML server-rendered.
- `DATABASE_URL` — variável de ambiente com a connection string do banco (ex.: PostgreSQL).

## Estrutura principal do projeto

- `app/main.py` — aplicação FastAPI e rotas
- `app/models.py` — modelos SQLAlchemy
- `app/schemas.py` — schemas Pydantic (requests/responses)
- `app/crud.py` — funções de acesso ao banco
- `app/database.py` — configuração do engine/Session e leitura de `.env`
- `templates/index.html` — página inicial renderizada

## Configuração e execução

1. Crie um ambiente virtual (recomendado) e instale dependências:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Configure a variável de ambiente `DATABASE_URL` (opcional). O projeto tenta carregar `.env` na raiz se existir. Exemplo de `DATABASE_URL`:

```text
postgresql://usuario:senha@localhost:5432/agenda_db
```

3. Criar tabelas: o projeto chama `Base.metadata.create_all(bind=engine)` automaticamente ao iniciar, assim as tabelas serão criadas se não existirem.

4. Rodar a API (desenvolvimento):

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Abra `http://127.0.0.1:8000/docs` para a interface Swagger ou `http://127.0.0.1:8000/redoc` para ReDoc.

## Notas de desenvolvimento

- A URL do banco é lida pela variável `DATABASE_URL`.
- As tabelas são criadas automaticamente na inicialização via SQLAlchemy `create_all` (sem migrações formais).
- Validações de entrada são feitas via Pydantic (schemas em `app/schemas.py`). Erros retornam respostas HTTP com detalhes.
