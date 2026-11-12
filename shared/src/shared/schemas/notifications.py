from pydantic import BaseModel
from shared.schemas.operations import OperationRead
from shared.schemas.accounts import AccountRead


class NotificationEvent(BaseModel):
    operation: OperationRead
    account: AccountRead