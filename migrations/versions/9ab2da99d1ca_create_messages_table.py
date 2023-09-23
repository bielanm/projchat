"""create_messages_table

Revision ID: 9ab2da99d1ca
Revises: 
Create Date: 2023-09-23 11:44:36.746575

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, TEXT, Column


# revision identifiers, used by Alembic.
revision: str = '9ab2da99d1ca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None





def upgrade() -> None:
    op.create_table(
        "message",
        Column("id", INTEGER, primary_key=True),
        Column("text", TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("messages")
