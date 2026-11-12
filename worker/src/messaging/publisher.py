from faststream.rabbit import RabbitBroker

from shared.messaging.exchange import loyalty_events_exchange
# from shared.schemas.events import OperationProcessedEvent
from shared.schemas.operations import OperationRead
from shared.schemas.events import OperationProcessedEvent


class Publisher:
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def publish_proccesed(
        self,
        event: OperationProcessedEvent,
    ) -> None:
        await self._broker.publish(
            message=event.model_dump(mode="json"),
            exchange=loyalty_events_exchange,
        )