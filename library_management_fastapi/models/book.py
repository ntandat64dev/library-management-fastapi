from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column, relationship

from library_management_fastapi.database import Base
from library_management_fastapi.models.genre import Genre


class Book(MappedAsDataclass, Base):
    __tablename__ = "book"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, insert_default=uuid4(), init=False
    )
    isbn: Mapped[str] = mapped_column(String(13), unique=True)
    title: Mapped[str]
    author: Mapped[str]
    publisher: Mapped[str]
    publish_date: Mapped[datetime]
    genre_id: Mapped[UUID] = mapped_column(ForeignKey("genre.id"))
    language: Mapped[str] = mapped_column(String(2))
    dimension: Mapped[str]
    total_copies: Mapped[int] = mapped_column()
    available_copies: Mapped[int] = mapped_column()
    genre: Mapped[Genre] = relationship(init=False, lazy="joined")
