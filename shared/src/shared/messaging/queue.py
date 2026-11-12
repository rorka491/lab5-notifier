from faststream.rabbit import RabbitQueue, QueueType
from shared.constants import Queue, RoutingKey


operations_queue = RabbitQueue(
    name=Queue.OPERATIONS,
    durable=True,
    queue_type=QueueType.QUORUM,
    routing_key=RoutingKey.OPERATION,
)

notifier_events_queue = RabbitQueue(
    name=Queue.NOTIFIER_EVENTS,
    durable=True,
    queue_type=QueueType.QUORUM
)

analytics_events_queue = RabbitQueue(
    name=Queue.ANALYTICS_EVENTS,
    durable=True,
    queue_type=QueueType.QUORUM
)