from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base


class Librarian(MappedAsDataclass, Base):
    __tablename__ = "librarian"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, insert_default=uuid4(), init=False
    )
    full_name: Mapped[str | None]
    email: Mapped[str] = mapped_column(unique=True)
    account_id: Mapped[UUID] = mapped_column(ForeignKey("account.id"))
