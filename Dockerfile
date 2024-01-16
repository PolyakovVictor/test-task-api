FROM python:latest

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY . .

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi