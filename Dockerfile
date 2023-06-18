# Imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo pyproject.toml e poetry.lock para o diretório de trabalho
COPY pyproject.toml poetry.lock /app/

# Instala as dependências do projeto usando o Poetry
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copia o código-fonte para o diretório de trabalho
COPY . /app/

# Expõe a porta do servidor web do Django
EXPOSE 8000

# Define o script como executável
RUN chmod +x run_manage.sh

# Executa os comandos desejados
CMD ["poetry","run", "./run_manage.sh", "makemigrations"]
CMD ["poetry","run",  "./run_manage.sh",  "migrate"]
CMD ["poetry","run",  "./run_manage.sh",  "runserver", "0.0.0.0:5000"]
