from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column


class AuditMixin:
    created_by: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    updated_by: Mapped[str | None]
    updated_at: Mapped[datetime | None]
