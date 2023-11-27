"""musicgenerator2

Revision ID: fc7d9f606dc5
Revises: 8c56dc420ecf
Create Date: 2023-11-08 17:38:25.538400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc7d9f606dc5'
down_revision: Union[str, None] = '8c56dc420ecf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'music_generator',
        sa.Column("key_words",sa.String, primary_key = True),
        sa.Column("user_id",sa.Integer, sa.ForeignKey('user.user_id'),primary_key = True),
        sa.Column("genres",sa.String),
        sa.Column("streaming_service_info",sa.String)
    )

def downgrade() -> None:
    op.drop_table("music_generator")
