from fastapi import FastAPI
from src.api import router
from dishka.integrations.fastapi import setup_dishka
from src.di.container import container
from src.lifespan import lifespan
from src.messaging.consumer import setup_consumers
from src.messaging.broker import broker

app = FastAPI(lifespan=lifespan)
app.include_router(router)
setup_consumers(broker)
setup_dishka(container, app)

