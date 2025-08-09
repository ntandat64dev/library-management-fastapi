from enum import Enum
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base
from library_management_fastapi.models.audit_mixin import AuditMixin


class MembershipStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Member(AuditMixin, MappedAsDataclass, Base):
    __tablename__ = "member"

    account_id: Mapped[UUID] = mapped_column(
        ForeignKey("account.id"),
        primary_key=True,
        init=False,
    )
    full_name: Mapped[str | None] = mapped_column(init=False)
    membership_status: Mapped[MembershipStatus] = mapped_column(
        insert_default=MembershipStatus.ACTIVE
    )
