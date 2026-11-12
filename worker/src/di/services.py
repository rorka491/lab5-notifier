from dishka import Provider, Scope, provide
from src.messaging.publisher import Publisher
from src.services import AccountService
from src.repositories import OperationRepository, AccountRepository


class ServiceProvider(Provider):

    # @provide(scope=Scope.REQUEST)
    # def operation_service(
    #     self,
    #     repo: OperationRepository,
    #     publisher: Publisher,
    # ) -> OperationService:
    #     return OperationService(repo=repo, publisher=publisher)

    @provide(scope=Scope.REQUEST)
    def account_service(
        self,
        repo: AccountRepository
    ) -> AccountService:
        return AccountService(repo=repo)