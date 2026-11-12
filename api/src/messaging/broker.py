from faststream.rabbit import RabbitBroker
from shared.config import rabbit_settings


broker = RabbitBroker(rabbit_settings.url)