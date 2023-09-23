"""add users table

Revision ID: e0e3b00be2be
Revises: 9ab2da99d1ca
Create Date: 2023-09-23 11:53:37.236682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0e3b00be2be'
down_revision: Union[str, None] = '9ab2da99d1ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
            sa.Column("id", sa.INTEGER, primary_key=True),
            sa.Column("username", sa.VARCHAR(32), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
