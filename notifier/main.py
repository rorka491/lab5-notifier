import asyncio
from faststream import FastStream
from src.messaging.consumer import setup_consumers
from src.messaging.broker import broker

app = FastStream(broker)
setup_consumers(broker)


asyncio.run(app.run())