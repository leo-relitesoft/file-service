FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV UV_NO_CACHE=1

COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen --no-install-project

COPY src /app/src/
COPY alembic /app/alembic/
COPY alembic.ini /app/
COPY docker/prod/entrypoint.sh /app/docker/entrypoint.sh
RUN chmod +x /app/docker/entrypoint.sh
RUN uv sync --frozen

EXPOSE 443 80

CMD ["/app/docker/entrypoint.sh"]