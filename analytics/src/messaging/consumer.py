from dishka import FromDishka
from faststream.rabbit import RabbitBroker
from dishka_faststream import inject
from shared.messaging.exchange import loyalty_commands_exchange
from shared.messaging.queue import operations_queue
from shared.schemas.events import OperationProcessedEvent
from src.services import AnalyticsService


def setup_consumers(broker: RabbitBroker) -> None:
    @broker.subscriber(
        queue=operations_queue,
        exchange=loyalty_commands_exchange,
    )
    @inject
    async def handle_operation(
        message: OperationProcessedEvent, 
        service: FromDishka[AnalyticsService],
    ) -> None:
        service.process(message)