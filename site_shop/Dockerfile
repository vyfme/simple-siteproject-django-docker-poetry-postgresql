FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /site_shop
RUN pip install poetry
COPY pyproject.toml poetry.lock /site_shop/
RUN poetry install --no-root
COPY . /site_shop/  
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true
ENTRYPOINT ["poetry", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]