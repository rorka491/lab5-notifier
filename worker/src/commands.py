from decimal import Decimal
from faststream.rabbit import RabbitBroker
from shared.models.account import Account
from shared.repositories import AccountRepository, OperationRepository
from shared.schemas.events import OperationProcessedEvent
from shared.schemas.notifications import NotificationEvent
from shared.schemas.operations import OperationCreate, OperationRead
from shared.transactions import SQLAlchemyTransaction
from shared.constants import OperationType, RejectReason, OperationStatus
from shared.schemas.accounts import AccountRead
from src.messaging.publisher import Publisher


class HandleOperationCommand:

    def __init__(
        self,
        transaction: SQLAlchemyTransaction,
        account_repo: AccountRepository,
        operation_repo: OperationRepository,
        publisher: Publisher
    ) -> None:
        self.transaction = transaction
        self.account_repo = account_repo
        self.operation_repo = operation_repo
        self.publisher = publisher

    async def execute(self, data: OperationCreate):
        async with self.transaction:
            account = await self.account_repo.get_for_update(id=data.account_id)
            if account is None:
                return
            if data.type == OperationType.PURCHASE:
                points_delta, reject_reason = self._process_purchase(data)
            elif data.type == OperationType.REDEEM:
                points_delta, reject_reason = self._process_redeem(data, account)
            elif data.type == OperationType.RETURN:
                points_delta, reject_reason = await self._process_return(data)
            else:
                raise ValueError(f"Unsupported operation type: {data.type}")
            
            if reject_reason is None:
                account.balance += points_delta
                status=OperationStatus.APPLIED
            else:
                status=OperationStatus.REJECTED

            operation = await self._save_operation(
                data=data,
                status=status,
                points_delta=points_delta,
                reject_reason=reject_reason,
                balance_after=account.balance,
            )
            await self.publisher.publish_proccesed(
                event=OperationProcessedEvent(
                    operation=OperationRead.model_validate(operation), 
                    account=AccountRead.model_validate(account)
                )
            )

        

    def _process_purchase(self, data: OperationCreate) -> tuple[int, RejectReason | None]:
        points = int(data.required_amount * Decimal("0.05"))
        return points, None

    def _process_redeem(
        self,
        data: OperationCreate,
        account: Account,
    ) -> tuple[int, RejectReason | None]:
        max_allowed_points = int(data.required_amount * Decimal("0.3"))
        if account.balance <= 0:
            return 0, RejectReason.INSUFFICIENT_BALANCE
        if account.balance < max_allowed_points:
            points_to_redeem = account.balance
        else:
            points_to_redeem = max_allowed_points
        return -points_to_redeem, None

    async def _process_return(
        self,
        data: OperationCreate,
    ) -> tuple[int, RejectReason | None]:
        purchase = await self.operation_repo.get_accepted_purchase(
            check_number=data.check_number,
        )
        if purchase is None:
            return 0, RejectReason.PURCHASE_NOT_FOUND
        already_returned = await self.operation_repo.has_returned_purchase(
            check_number=data.check_number,
        )
        if already_returned:
            return 0, RejectReason.ALREADY_RETURNED
        return -purchase.points_delta, None        

    async def _save_operation(
        self,
        data: OperationCreate,
        points_delta: int,
        status: OperationStatus,
        balance_after: int,
        reject_reason: RejectReason | None,
    ):
        return await self.operation_repo.create(
            type=data.type,
            account_id=data.account_id,
            store_id=data.store_id,
            status=status,
            check_number=data.check_number,
            points_delta=points_delta,
            balance_after=balance_after,
            reject_reason=reject_reason,
            amount=data.amount,
        )