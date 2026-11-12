from uuid import UUID
from shared.exceptions import ObjectNotFound 
from shared.schemas.operations import OperationCreate
from src.models import Operation, Account
from src.repositories import OperationRepository, AccountRepository
from src.messaging.publisher import Publisher


class OperationService:

    def __init__(self, repo: OperationRepository, publisher: Publisher) -> None:
        self.publisher = publisher
        self.repo = repo

    async def create(self, data: OperationCreate): 
        await self.publisher.publish_operation(data)

    async def get_by_id(self, id: UUID) -> Operation:
        operation = await self.repo.get_by_id(id)
        if operation is None:
            raise ObjectNotFound()
        return operation


class AccountService:

    def __init__(self, repo: AccountRepository):
        self.repo = repo

    async def create(self) -> Account:
        return await self.repo.create()
        
    async def get_by_id(self, id: UUID) -> Account:
        account = await self.repo.get_by_id(id)
        if account is None:
            raise ObjectNotFound()
        return account