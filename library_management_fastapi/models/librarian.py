from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base
from library_management_fastapi.models.audit_mixin import AuditMixin


class Librarian(AuditMixin, MappedAsDataclass, Base):
    __tablename__ = "librarian"

    account_id: Mapped[UUID] = mapped_column(
        ForeignKey("account.id"),
        primary_key=True,
        init=False,
    )
    full_name: Mapped[str | None]
