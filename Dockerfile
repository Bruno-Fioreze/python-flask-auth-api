FROM python:3.10-slim-buster

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main

COPY . .

EXPOSE 8000

CMD ["/app/launcher.sh"]
