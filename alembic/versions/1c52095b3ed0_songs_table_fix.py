"""songs table fix

Revision ID: 1c52095b3ed0
Revises: fc7d9f606dc5
Create Date: 2023-11-20 13:10:42.759339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c52095b3ed0'
down_revision: Union[str, None] = 'fc7d9f606dc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # with op.batch_alter_table('ps_endpoints') as batch_op:
    #     batch_op.alter_column('accountcode', type_=sa.String(80))
    # with op.batch_alter_table('sippeers') as batch_op:
    #     batch_op.alter_column('accountcode', type_=sa.String(80))
    # with op.batch_alter_table('iaxfriends') as batch_op:
    #     batch_op.alter_column('accountcode', type_=sa.String(80))
    with op.batch_alter_table("songs") as batch_op:
        batch_op.drop_column("song_name")
        batch_op.add_column(sa.Column("song_name",sa.String))
        batch_op.add_column(sa.Column('song_id', sa.Integer, primary_key=True, autoincrement=True))
    
    op.create_unique_constraint('uq_song_id', 'songs', ['song_id'])


def downgrade() -> None:
    # op.drop_constraint('uq_song_id', 'your_table_name', type_='unique')
    # op.drop_column('songs', 'song_id')
    pass