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

CMD ['cd', '']
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

