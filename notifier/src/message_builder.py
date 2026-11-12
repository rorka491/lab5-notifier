from shared.constants import OperationStatus, OperationType
from shared.schemas.events import OperationProcessedEvent


class MessageBuilder:

    def build(self, event: OperationProcessedEvent) -> str:
        if event.operation.status == OperationStatus.REJECTED:
            if event.operation.reject_reason is None:
                raise ValueError("Rejected operation must have a reject reason")

            return f"Операция отклонена: {event.operation.reject_reason}"

        if event.operation.type == OperationType.PURCHASE:
            return (
                f"Начислено {event.operation.points_delta} баллов, "
                f"баланс {event.operation.balance_after}"
            )

        if event.operation.type in (OperationType.REDEEM, OperationType.RETURN):
            return (
                f"Списано {abs(event.operation.points_delta)} баллов, "
                f"баланс {event.operation.balance_after}"
            )

        raise ValueError(f"Unsupported operation type: {event.operation.type}")