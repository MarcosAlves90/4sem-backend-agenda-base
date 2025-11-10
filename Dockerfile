FROM python:3.11-slim

# Evita criação de .pyc e deixa saída do Python sem buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema necessárias para alguns pacotes (ex.: psycopg2)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia só requirements para aproveitar cache do Docker
COPY requirements.txt /app/requirements.txt

# Cria uma virtualenv dedicada e instala as dependências nela.
# Usar uma venv evita instalar pacotes no site-packages do sistema e é a
# forma recomendada para evitar conflitos e avisos ao rodar pip como root.
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

# Garante que a venv esteja no PATH para comandos em tempo de execução
ENV PATH="/opt/venv/bin:$PATH"

# Copia o código da aplicação
COPY . /app

# Cria e configura usuário não-root, e garante permissões sobre /app e a venv
RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app /opt/venv

USER appuser

EXPOSE 8000

# Comando padrão para executar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
