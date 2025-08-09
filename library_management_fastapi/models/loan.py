from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base
from library_management_fastapi.models.audit_mixin import AuditMixin


class LoanStatus(Enum):
    BORROWED = "BORROWED"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class Loan(AuditMixin, MappedAsDataclass, Base):
    __tablename__ = "loan"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, insert_default=uuid4(), init=False
    )
    book_id: Mapped[UUID] = mapped_column(ForeignKey("book.id"))
    member_id: Mapped[UUID] = mapped_column(ForeignKey("member.account_id"))
    loan_date: Mapped[datetime]
    fine_amount: Mapped[float]
    status: Mapped[LoanStatus] = mapped_column(insert_default=LoanStatus.BORROWED)
