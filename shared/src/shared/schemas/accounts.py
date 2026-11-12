from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field
from shared.schemas.operations import OperationRead



class AccountCreate(BaseModel):
    email: str

class AccountRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    balance: int
    email: str
    send_email_allow: bool



class AccountDetail(AccountRead):
    operations: list[OperationRead] = Field(default_factory=list)

