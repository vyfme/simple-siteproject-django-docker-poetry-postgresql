FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /site_shop

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml /site_shop/

RUN poetry install --no-root --no-interaction --no-ansi

COPY . /site_shop/  

RUN poetry config virtualenvs.create false

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]