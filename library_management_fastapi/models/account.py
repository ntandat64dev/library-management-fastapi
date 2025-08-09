from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base
from library_management_fastapi.models.audit_mixin import AuditMixin


class Account(AuditMixin, MappedAsDataclass, Base):
    __tablename__ = "account"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, insert_default=uuid4(), init=False
    )
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
