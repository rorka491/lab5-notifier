from datetime import UTC, datetime
from decimal import Decimal
from typing import Optional
import uuid
from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from shared.models.base import Base, BaseModelPK
from shared.models.account import Account
from shared.constants import OperationStatus, OperationType, RejectReason


class Operation(BaseModelPK):
    __tablename__ = "operations"

    type: Mapped[OperationType] = mapped_column(String(20), nullable=False)
    account_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False,
        index=True,
    )
    store_id: Mapped[str] = mapped_column(String(100), nullable=False)
    check_number: Mapped[str] = mapped_column(String(100), nullable=False)
    amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    # points: Mapped[Optional[int]] = mapped_column(BigInteger)
    status: Mapped[OperationStatus] = mapped_column(String(20), nullable=False)
    points_delta: Mapped[int] = mapped_column(BigInteger, nullable=False)
    balance_after: Mapped[int] = mapped_column(BigInteger, nullable=False)
    reject_reason: Mapped[Optional[RejectReason]] = mapped_column(
        String(50),
        nullable=True,
    )

    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
    processed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    account: Mapped[Account] = relationship("Account", back_populates="operations")
