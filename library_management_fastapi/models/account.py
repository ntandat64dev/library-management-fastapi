from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from library_management_fastapi.database import Base


class Account(MappedAsDataclass, Base):
    __tablename__ = "account"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, insert_default=uuid4(), init=False
    )
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
