"""clone postgresql db to mysql db

Revision ID: 66148bab10cb
Revises: 8f087ec4cb82
Create Date: 2024-03-30 17:24:50.717711

"""
from typing import Sequence, Union

from alembic import op
import alembic as al
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66148bab10cb'
down_revision: Union[str, None] = '8f087ec4cb82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    source_db_uri = al.context.config.get_main_option('source_db_uri')
    destination_db_uri = al.context.config.get_main_option('destination_db_uri')

    source_engine = sa.create_engine(source_db_uri)
    destination_engine = sa.create_engine(destination_db_uri)

    source_conn = source_engine.connect()
    source_metadata = sa.MetaData()
    source_metadata.reflect(bind=source_engine)
    source_table = sa.Table('weather', source_metadata)
    source_data = source_conn.execute(source_table.select()).fetchall()

    destination_conn = destination_engine.connect()
    destination_metadata = sa.MetaData()
    destination_table = sa.Table('weather', destination_metadata,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('country', sa.Text(), nullable=True),
        sa.Column('wind_mph', sa.DECIMAL(), nullable=True),
        sa.Column('wind_kph', sa.DECIMAL(), nullable=True),
        sa.Column('wind_degree', sa.Integer(), nullable=True),
        sa.Column('wind_direction', sa.Enum('SSE', 'NW', 'W', 'NE', 'SE', 'WNW', 'N', 'NNW', 'E', 'WSW', 'NNE', 'ENE', 'SW', 'S', 'SSW', 'ESE', name='direction', create_type=False), nullable=True),
        sa.Column('last_updated', sa.DateTime(), nullable=True),
        sa.Column('sunrise', sa.Time(), nullable=True),
        sa.Column('should_go_out', sa.Boolean(), nullable=True),
        )
    destination_metadata.create_all(destination_engine)
    destination_conn.execute(destination_table.insert(), [row._asdict() for row in source_data])

def downgrade() -> None:
    destination_db_uri = al.context.config.get_main_option('destination_db_uri')
    destination_engine = sa.create_engine(destination_db_uri)
    destination_metadata = sa.MetaData()
    destination_metadata.reflect(bind=destination_engine)
    destination_metadata.drop_all(destination_engine, checkfirst=True)
