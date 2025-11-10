
# API Base Agenda

Uma API simples para gerenciar alunos e uma agenda escolar. A aplicação fornece endpoints REST para criar, listar, atualizar e deletar alunos e entradas de agenda. É construída com FastAPI, SQLAlchemy e Pydantic.

## Principais funcionalidades

- CRUD de Alunos (nome, email, data de nascimento)
- CRUD de Entradas de Agenda (data, hora de início, hora de fim, descrição, referência a turma/disciplina/professor)
- Página inicial renderizada com Jinja2 em `/` (arquivo `templates/index.html`)
- Documentação automática via Swagger (OpenAPI) e ReDoc gerada pelo FastAPI

## Tech stack

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Jinja2 (templates)
- Banco de dados configurável via variável de ambiente `DATABASE_URL` (por padrão o projeto tenta usar PostgreSQL)

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

## Endpoints principais

Todos os endpoints seguem padrão REST e retornam/recebem JSON quando aplicável.

Alunos

- POST /alunos/ — cria um aluno
- GET  /alunos/ — lista todos os alunos
- GET  /alunos/{aluno_id} — obtém um aluno por ID
- PUT  /alunos/{aluno_id} — atualiza um aluno
- DELETE /alunos/{aluno_id} — deleta um aluno

Agenda

- POST /agenda/ — cria uma entrada de agenda
- GET  /agenda/ — lista todas as entradas
- GET  /agenda/{agenda_id} — obtém uma entrada por ID
- PUT  /agenda/{agenda_id} — atualiza uma entrada
- DELETE /agenda/{agenda_id} — deleta uma entrada

Homepage

- GET / — renderiza `templates/index.html` (página inicial com links úteis)

## Schemas (resumo)

Aluno (requests/responses):

- nome: string
- email: string (formato email)
- data_nascimento: date (opcional)

Resposta de leitura (`AlunoRead`) inclui `id` além desses campos.

Agenda (requests/responses):

- data: date (YYYY-MM-DD)
- hora_inicio: time (HH:MM:SS)
- hora_fim: time (HH:MM:SS)
- descricao: string (opcional)
- turma_id, disciplina_id, professor_id: int (opcionais)

Resposta de leitura (`AgendaRead`) inclui `id` além dos campos acima.

## Exemplos de uso (curl)

Criar um aluno:

```bash
curl -X POST "http://127.0.0.1:8000/alunos/" -H "Content-Type: application/json" -d \
'{"nome": "João Silva", "email": "joao@example.com", "data_nascimento": "2005-04-10"}'
```

Listar alunos:

```bash
curl http://127.0.0.1:8000/alunos/
```

Criar uma entrada na agenda:

```bash
curl -X POST "http://127.0.0.1:8000/agenda/" -H "Content-Type: application/json" -d \
'{"data": "2025-11-10", "hora_inicio": "09:00:00", "hora_fim": "10:00:00", "descricao": "Aula de Matemática"}'
```

## Notas de desenvolvimento

- A URL do banco é lida pela variável `DATABASE_URL`. Se preferir usar SQLite para testes locais, ajuste `DATABASE_URL` para algo como `sqlite:///./test.db` e adapte o `create_engine` se necessário.
- As tabelas são criadas automaticamente na inicialização via SQLAlchemy `create_all` (sem migrações formais). Para projetos em produção, considere usar Alembic para migrações.
- Validações de entrada são feitas via Pydantic (schemas em `app/schemas.py`). Erros retornam respostas HTTP com detalhes.

## Testes e scripts

- Há um script de exemplo `scripts/test_render.py` (verificar conteúdo) — use-o como referência para renderização de templates/local tests.

## Contribuição

Pull requests são bem-vindos. Para mudanças significativas, abra uma issue primeiro para discutir o que quer alterar.

## Licença

Use conforme sua necessidade. Adicione um arquivo LICENSE se desejar especificar termos.
