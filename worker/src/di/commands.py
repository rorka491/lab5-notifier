from dishka import Provider, Scope, provide
from shared.repositories import AccountRepository, OperationRepository
from shared.transactions import SQLAlchemyTransaction
from src.messaging.publisher import Publisher
from src.commands import HandleOperationCommand

class CommandProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def handle_operation(
        self,
        transaction: SQLAlchemyTransaction,
        account_repo: AccountRepository,
        operation_repo: OperationRepository,
        publisher: Publisher,
    ) -> HandleOperationCommand:
        return HandleOperationCommand(
            transaction=transaction,
            account_repo=account_repo,
            operation_repo=operation_repo,
            publisher=publisher,
        )