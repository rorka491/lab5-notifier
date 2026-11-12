from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.messaging.broker import broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.stop()