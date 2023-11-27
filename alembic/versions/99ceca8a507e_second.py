"""second

Revision ID: 99ceca8a507e
Revises: 7ae9fabbac30
Create Date: 2023-11-08 16:48:52.251973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99ceca8a507e'
down_revision: Union[str, None] = '7ae9fabbac30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column("user_id",sa.Integer, primary_key = True),
        sa.Column("email",sa.String),
        sa.Column("library_id",sa.Integer, sa.ForeignKey('Music_Library.user_id')),
        sa.Column("phone_number",sa.String)
    )


def downgrade() -> None:
    op.drop_table("user")
