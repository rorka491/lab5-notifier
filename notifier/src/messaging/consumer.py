from logging import getLogger
from faststream.rabbit import RabbitBroker
from dishka_faststream import inject
from shared.messaging.exchange import loyalty_events_exchange
from shared.messaging.queue import notifier_events_queue
from shared.schemas.events import OperationProcessedEvent
from src.message_builder import MessageBuilder
from src.email_sender import EmailSender
from src.config import settings


sender = EmailSender(
    host=settings.email_host,
    port=settings.email_port,
    username=settings.email_username,
    password=settings.email_password
)

msg_builder = MessageBuilder()

def setup_consumers(broker: RabbitBroker) -> None:
    @broker.subscriber(
        queue=notifier_events_queue,
        exchange=loyalty_events_exchange,
    )
    @inject
    async def handle_operation(message: OperationProcessedEvent) -> None:
        if message.account.send_email_allow:
            body = msg_builder.build(message)
            await sender.send(
                recipient=message.account.email,
                body=body,
                subject="Loyalty notification"
            )