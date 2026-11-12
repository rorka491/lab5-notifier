from logging import getLogger
from faststream.rabbit import RabbitBroker
from dishka import FromDishka
from dishka_faststream import inject
from shared.messaging.exchange import loyalty_commands_exchange
from shared.messaging.queue import operations_queue
from shared.schemas.operations import OperationCreate
from src.commands import HandleOperationCommand

logger = getLogger(__name__)

def setup_consumers(broker: RabbitBroker) -> None:
    @broker.subscriber(
        queue=operations_queue,
        exchange=loyalty_commands_exchange,
    )
    @inject
    async def handle_operation(
        message: OperationCreate, 
        command: FromDishka[HandleOperationCommand]
    ) -> None:
        await command.execute(message)




