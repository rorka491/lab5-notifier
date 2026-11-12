from dishka import Provider, Scope, provide
from shared.repositories import AccountRepository
from shared.transactions import SQLAlchemyTransaction
from src.messaging.publisher import Publisher
from src.messaging.broker import broker
from src.commands import CreateAccountCommand


class CommandProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def handle_operation(
        self,
        transaction: SQLAlchemyTransaction,
        account_repo: AccountRepository,
    ) -> CreateAccountCommand:
        return CreateAccountCommand(
            transaction=transaction,
            account_repo=account_repo
        )