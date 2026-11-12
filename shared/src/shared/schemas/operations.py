from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict, model_validator
from shared.constants import OperationStatus, OperationType, RejectReason


class OperationCreate(BaseModel):
    type: OperationType
    account_id: UUID
    store_id: str = Field(min_length=1, max_length=100)
    check_number: str = Field(min_length=1, max_length=100)
    amount: Decimal | None = Field(default=None, gt=0)

    @property
    def required_amount(self) -> Decimal:
        if self.amount:
            return self.amount
        raise ValueError("Amount is None")
        
    
    @model_validator(mode="after")
    def validate_amount(self):
        if self.type in (OperationType.PURCHASE, OperationType.REDEEM):
            if self.amount is None:
                raise ValueError("amount is required")
        elif self.type == OperationType.RETURN:
            if self.amount is not None:
                raise ValueError("amount must be absent for return")

        return self


class OperationRead(BaseModel):
    id: UUID
    type: OperationType
    account_id: UUID
    store_id: str = Field(min_length=1, max_length=100)
    check_number: str = Field(min_length=1, max_length=100)
    amount: Decimal | None = Field(default=None, gt=0)
    occurred_at: datetime
    status: OperationStatus
    points_delta: int
    balance_after: int
    reject_reason: RejectReason | None
    processed_at: datetime

    model_config = ConfigDict(from_attributes=True)