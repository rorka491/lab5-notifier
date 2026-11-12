import asyncio
import logging
from faststream import FastStream
from dishka_faststream import setup_dishka
from src.messaging.consumer import setup_consumers
from src.messaging.broker import broker
from src.di.container import container 


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

app = FastStream(broker)
setup_dishka(container, app)
setup_consumers(broker)


asyncio.run(app.run())