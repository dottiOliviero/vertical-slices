ARG python_version=3.10
ARG poetry_version=1.3.2

FROM python:${python_version}-buster as base

RUN pip install poetry==1.3.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY poetry.lock pyproject.toml ./


# Setup the essential dependencies for your psycopg2 library
RUN apt-get update \ 
&& apt-get install -y build-essential libpq-dev gcc \ 
&& rm -rf /var/lib/apt/lists/*

RUN poetry install --no-root --no-dev && rm -rf $POETRY_CACHE_DIR

################################################################################

FROM base as development

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=base ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# copy everything before installing dependencies, to let poetry install all the dependencies
COPY . .
# Install the development dependencies as well in our development target.
RUN poetry install --no-root


################################################################################

FROM python:${python_version}-slim-buster as production

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=base ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app ./app
