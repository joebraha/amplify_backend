"""musicgenerator

Revision ID: 8c56dc420ecf
Revises: 14d321eeafba
Create Date: 2023-11-08 17:06:16.986014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c56dc420ecf'
down_revision: Union[str, None] = '14d321eeafba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'streaming_service',
        sa.Column("user_id",sa.Integer, sa.ForeignKey('user.user_id'), primary_key = True),
        sa.Column("email",sa.String),
        sa.Column("service_songs",sa.String),
        sa.Column("service_password",sa.String),
        sa.Column("service_username",sa.String),
        sa.Column("service_name",sa.String,primary_key = True),
    )


def downgrade() -> None:
    op.drop_table("streaming_service")
