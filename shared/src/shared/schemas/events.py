from pydantic import BaseModel
from datetime import datetime
from shared.constants import OperationStatus, OperationType, RejectReason
from shared.schemas.operations import OperationRead
from shared.schemas.accounts import AccountRead

class OperationProcessedEvent(BaseModel):
    operation: OperationRead
    account: AccountRead    



    