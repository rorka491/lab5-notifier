from collections import defaultdict
from uuid import UUID

from shared.constants import OperationType


class StoreStats:
    def __init__(self, store_id: str) -> None:
        self.store_id = store_id
        self.accepted_operations: dict[OperationType, int] = defaultdict(int)
        self.rejected_operations = 0
        self.earned_points = 0
        self.returned_points = 0
        self.spent_points = 0


class StatsRepository:

    def __init__(self) -> None:
        self._stores: dict[str, StoreStats] = {}
        self._events_count = 0

    def get(self, store_id: str) -> StoreStats | None:
        return self._stores.get(store_id)

    def get_all(self) -> list[StoreStats]:
        return list(self._stores.values())

    def get_or_create(self, store_id: str) -> StoreStats:
        if store_id not in self._stores:
            self._stores[store_id] = StoreStats(store_id)

        return self._stores[store_id]

    def increment_events_count(self) -> None:
        self._events_count += 1

    def get_events_count(self) -> int:
        return self._events_count