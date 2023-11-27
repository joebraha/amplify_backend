"""init

Revision ID: 7ae9fabbac30
Revises: 
Create Date: 2023-11-08 13:27:50.389525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ae9fabbac30'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Music_Library',
        sa.Column("songs",sa.Integer),
        sa.Column("storage_used",sa.Integer),
        sa.Column("user_id",sa.Integer, primary_key = True,),
        sa.Column("storage_left",sa.Integer)
    )

    # op.create_table(
    #     'user',
    #     sa.Column("user_id",sa.Integer, primary_key = True),
    #     sa.Column("email",sa.String),
    #     sa.Column("library_id",sa.Integer, sa.ForeignKey('music_library.user_id')),
    #     sa.Column("phone_number",sa.String)
    # )
    
    # op.create_table(
    #     'songs',
    #     sa.Column("song_name",sa.String, primary_key = True),
    #     sa.Column("length",sa.String),
    #     sa.Column("user_id",sa.Integer, sa.ForeignKey('user.user_id'), primary_key = True),
    #     sa.Column("genre",sa.String)
    # )

    # op.create_table(
    #     'music_generator',
    #     sa.Column("key_words",sa.String, primary_key = True),
    #     sa.Column("user_id",sa.Integer, sa.ForeignKey('songs.user_id'),primary_key = True),
    #     sa.Column("genres",sa.String),
    #     sa.Column("streaming_service_info",sa.String)
    # )

    # op.create_table(
    #     'streaming_service',
    #     sa.Column("user_id",sa.Integer, sa.ForeignKey('user.user_id'), primary_key = True),
    #     sa.Column("email",sa.String),
    #     sa.Column("service_songs",sa.String),
    #     sa.Column("service_password",sa.String),
    #     sa.Column("service_username",sa.String),
    #     sa.Column("service_name",sa.String,primary_key = True),
    # )


def downgrade() -> None:
    # op.drop_table("songs")

    # op.drop_table("music_generator")

    # op.drop_table("user")

    # op.drop_table("streaming_service")

    op.drop_table("Music_Library")

