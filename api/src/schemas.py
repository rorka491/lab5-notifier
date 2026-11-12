from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict
from shared.constants import OperationType


# class OperationCreate(BaseModel):
#     type: OperationType
#     customer_id: str = Field(min_length=1, max_length=100)
#     store_id: str = Field(min_length=1, max_length=100)
#     check_number: str = Field(min_length=1, max_length=100)
#     amount: Decimal | None = Field(default=None, gt=0)
#     points: int | None = Field(default=None, gt=0)
#     occurred_at: datetime


# class OperationRead(BaseModel):
#     id: UUID
#     type: OperationType
#     customer_id: str = Field(min_length=1, max_length=100)
#     store_id: str = Field(min_length=1, max_length=100)
#     check_number: str = Field(min_length=1, max_length=100)
#     amount: Decimal | None = Field(default=None, gt=0)
#     points: int | None = Field(default=None, gt=0)
#     occurred_at: datetime

#     model_config = ConfigDict(from_attributes=True)

class AccountRead(BaseModel):
    id: UUID
    balance: int
