from faststream.rabbit import RabbitExchange, ExchangeType
from shared.constants import Exchange

loyalty_commands_exchange = RabbitExchange(
    name=Exchange.LOYALTY_COMMANDS,
    type=ExchangeType.DIRECT,
    durable=True,
)

loyalty_events_exchange = RabbitExchange(
    name=Exchange.LOYALTY_EVENTS,
    type=ExchangeType.FANOUT,
    durable=True,
)