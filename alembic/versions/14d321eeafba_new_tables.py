"""new tables

Revision ID: 14d321eeafba
Revises: 99ceca8a507e
Create Date: 2023-11-08 17:03:46.781120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14d321eeafba'
down_revision: Union[str, None] = '99ceca8a507e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'songs',
        sa.Column("song_name",sa.String, primary_key = True),
        sa.Column("length",sa.String),
        sa.Column("user_id",sa.Integer, sa.ForeignKey('user.user_id'), primary_key = True),
        sa.Column("genre",sa.String),
    )
2
def downgrade() -> None:
    op.drop_table("songs")
