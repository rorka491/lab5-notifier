from faststream.rabbit import RabbitBroker
from src.core import rabbit_settings

broker = RabbitBroker(rabbit_settings.url)