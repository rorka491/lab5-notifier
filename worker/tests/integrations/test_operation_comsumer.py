from decimal import Decimal
from uuid import uuid4

from shared.constants import OperationType

import pytest
from unittest.mock import AsyncMock

from faststream.rabbit import RabbitBroker, TestRabbitBroker

from shared.schemas.operations import OperationCreate
from shared.messaging.exchange import loyalty_commands_exchange
from shared.messaging.queue import operations_queue


@pytest.mark.asyncio
async def test_operation_consumer():
    broker = RabbitBroker()

    command = AsyncMock()

    # Здесь регистрируем consumer с тестовой зависимостью.
    # Для этого нужно подключить тестовый Dishka container.

    async with TestRabbitBroker(broker) as test_broker:
        account_id = uuid4()
        message = OperationCreate(
            type=OperationType.PURCHASE,
            account_id=account_id,
            store_id="store-001",
            check_number="check-001",
            amount=Decimal("1000.00"),
        )

        await test_broker.publish(
            message,
            queue=operations_queue,
            exchange=loyalty_commands_exchange,
        )

    command.execute.assert_awaited_once_with(message)