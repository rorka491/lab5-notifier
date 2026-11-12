
from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Integer, true, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from shared.models.base import BaseModelPK
from shared.constants import OperationStatus, OperationType, RejectReason

if TYPE_CHECKING:
    from shared.models.operation import Operation

class Account(BaseModelPK):
    __tablename__ = "accounts"

    balance: Mapped[int] = mapped_column(
        Integer, 
        nullable=False, 
        default=0
    )
    send_email_allow: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=true()
    )
    email: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )
    operations: Mapped[list["Operation"]] = relationship(
        back_populates="account"
    )