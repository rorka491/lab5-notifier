from shared.constants import OperationType, OperationStatus
from shared.schemas.events import OperationProcessedEvent
from src.repositories import StatsRepository


class AnalyticsService:

    def __init__(self, repository: StatsRepository) -> None:
        self.repository = repository

    def process(self, event: OperationProcessedEvent) -> None:
        operation = event.operation

        stats = self.repository.get_or_create(operation.store_id)
        self.repository.increment_events_count()

        if operation.status == OperationStatus.REJECTED:
            stats.rejected_operations += 1
            return

        stats.accepted_operations[operation.type] += 1

        points = abs(operation.points_delta)

        match operation.type:
            case OperationType.PURCHASE:
                stats.earned_points += points

            case OperationType.RETURN:
                stats.returned_points += points

            case OperationType.REDEEM:
                stats.spent_points += points