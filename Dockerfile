FROM python:3.11-slim

# Evita criação de .pyc e deixa saída do Python sem buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema necessárias para alguns pacotes (ex.: psycopg2)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia só requirements e instala dependências antes de copiar todo o projeto
# para aproveitar cache do Docker
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copia o código da aplicação
COPY . /app

# Executa como usuário não-root
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# Comando padrão para executar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
