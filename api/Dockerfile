FROM python:3.13-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY shared /app/shared
COPY api /app/api

WORKDIR /app/api
RUN uv sync --no-dev

COPY api/entrypoint.sh /app/api/entrypoint.sh
RUN chmod +x /app/api/entrypoint.sh

ENTRYPOINT ["/app/api/entrypoint.sh"]

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]