from shared.models.account import Account
from shared.repositories import AccountRepository
from shared.schemas.accounts import AccountRead, AccountCreate
from shared.transactions import SQLAlchemyTransaction

class CreateAccountCommand:

    def __init__(
        self,
        transaction: SQLAlchemyTransaction,
        account_repo: AccountRepository,
    ) -> None:
        self.transaction = transaction
        self.account_repo = account_repo

    async def execute(self, data: AccountCreate) -> Account:
        async with self.transaction:
            return await self.account_repo.create(**data.model_dump())
    