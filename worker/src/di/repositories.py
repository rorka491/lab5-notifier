from dishka import Provider, Scope, provide
from src.repositories import OperationRepository, AccountRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Operation, Account

class RepositoryProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def operation_repo(
        self,
        session: AsyncSession
    ) -> OperationRepository:
        return OperationRepository(
            session=session,
            model=Operation
        )

    @provide(scope=Scope.REQUEST)
    def account_repo(
        self,
        session: AsyncSession
    ) -> AccountRepository:
        return AccountRepository(
            session=session,
            model=Account
        )