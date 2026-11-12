FROM python:3.13-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY shared /app/shared
COPY worker /app/worker

WORKDIR /app/worker
RUN uv sync --no-dev

CMD ["uv", "run", "python", "main.py"]