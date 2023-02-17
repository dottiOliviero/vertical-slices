ARG python_version=3.9.13
ARG poetry_version=1.3.2

FROM baseImage

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

COPY app /app/app/
COPY alembic  /app/alembic/
COPY alembic.ini /app/


USER nobody

WORKDIR /app