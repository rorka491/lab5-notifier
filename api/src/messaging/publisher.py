from faststream.rabbit import RabbitBroker
from shared.schemas.operations import OperationCreate
from shared.constants import Exchange, RoutingKey, Queue
from shared.schemas.operations import OperationCreate
from shared.messaging.queue import operations_queue
from shared.messaging.exchange import loyalty_commands_exchange


class Publisher:
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def publish_operation(self, data: OperationCreate) -> None:
        await self._broker.publish(
            message=data.model_dump(mode="json"),
            routing_key=RoutingKey.OPERATION,
            exchange=loyalty_commands_exchange
        )

