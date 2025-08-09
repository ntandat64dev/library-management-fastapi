"""update member and librarian primary key

Revision ID: 3a9313e97e95
Revises: b0240709d3a1
Create Date: 2025-08-09 20:53:22.940026

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3a9313e97e95"
down_revision: Union[str, Sequence[str], None] = "b0240709d3a1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(op.f("loan_member_id_fkey"), "loan")
    op.drop_column("librarian", "id")
    op.drop_column("member", "id")
    op.create_primary_key(None, "member", ["account_id"])
    op.create_primary_key(None, "librarian", ["account_id"])
    op.create_foreign_key(None, "loan", "member", ["member_id"], ["account_id"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("loan_member_id_fkey"), "loan")
    op.add_column("member", sa.Column("id", sa.Uuid))
    op.add_column("librarian", sa.Column("id", sa.Uuid))
    op.drop_constraint(op.f("member_pkey"), "member")
    op.drop_constraint(op.f("librarian_pkey"), "librarian")
    op.create_primary_key(None, "member", ["id"])
    op.create_primary_key(None, "librarian", ["id"])
    op.create_foreign_key(None, "loan", "member", ["member_id"], ["id"])
