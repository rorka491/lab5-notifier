from decimal import Decimal
from uuid import UUID
import uuid
from shared.schemas.accounts import AccountCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from shared.constants import OperationStatus, OperationType, RejectReason, OperationStatus
from shared.models import Account, Operation
from shared.transactions import SQLAlchemyTransaction

class AccountRepository:
    def __init__(self, session: AsyncSession, model: type[Account]) -> None:
        self._session = session
        self.model = model

    async def get_by_id(self, id: UUID) -> Account | None:
        statement = (
            select(self.model)
            .where(self.model.id == id)
            .options(selectinload(self.model.operations))
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()

    async def get_for_update(self, id: UUID) -> Account | None:
        statement = (
            select(self.model)
            .where(self.model.id == id)
            .with_for_update()
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()

    async def add(self, account: Account) -> None:
        self._session.add(account)
        await self._session.flush()

    async def create(self, email: str) -> Account:
        account = Account(email=email)
        await self.add(account)
        return account


class OperationRepository:
    def __init__(self, session: AsyncSession, model: type[Operation]) -> None:
        self._session = session
        self.model = model

    async def create(
        self,
        type: OperationType,
        account_id: uuid.UUID,
        store_id: str,
        status: OperationStatus,
        check_number: str,
        points_delta: int,
        balance_after: int,
        reject_reason: RejectReason | None = None,
        amount: Decimal | None = None,
    ) -> Operation:
        operation = Operation(
            type=type,
            account_id=account_id,
            store_id=store_id,
            status=status,
            check_number=check_number,
            points_delta=points_delta,
            balance_after=balance_after,
            reject_reason=reject_reason, 
            amount=amount
        )
        await self.add(operation)
        return operation

    async def get_by_id(self, id: UUID) -> Operation | None:
        statement = select(self.model).where(self.model.id == id)
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()


    async def get_accepted_purchase(
        self,
        check_number: str,
    ) -> Operation | None:
        statement = select(self.model).where(
            self.model.check_number == check_number,
            self.model.type == OperationType.PURCHASE,
            self.model.status == OperationStatus.APPLIED,
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()

    async def has_returned_purchase(self, check_number: str) -> bool:
        statement = select(self.model.id).where(
            self.model.check_number == check_number,
            self.model.type == OperationType.RETURN,
            self.model.status == OperationStatus.APPLIED,
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none() is not None

    async def add(self, operation: Operation) -> None:
        self._session.add(operation)
        await self._session.flush()