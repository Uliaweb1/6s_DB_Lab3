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
    # Get connection strings from Alembic configuration
    source_db_uri = al.context.config.get_main_option('source_db_uri')
    destination_db_uri = al.context.config.get_main_option('destination_db_uri')

    # Connect to source and destination databases
    source_engine = sa.create_engine(source_db_uri)
    destination_engine = sa.create_engine(destination_db_uri)

    # Query data from source database
    # source_conn = source_engine.connect()
    # source_session = sa.orm.sessionmaker(bind=engine)
    # source_metadata = sa.MetaData(bind=source_conn)
    source_metadata = sa.MetaData()
    source_metadata.reflect(bind=source_engine)
    # source_table = sa.Table('weather', source_metadata, autoload=True)
    # source_table = sa.Table('weather', source_metadata)
    # source_data = source_conn.execute(source_table.select()).fetchall()

    # Insert data into destination database
    # destination_conn = destination_engine.connect()
    tables_to_migrate = [source_metadata.tables["weather"]]
    source_metadata.create_all(destination_engine, tables_to_migrate)
    # destination_table = sa.Table('weather', destination_metadata, autoload=True)
    # destination_conn.execute(destination_table.insert(), [dict(row) for row in source_data])


def downgrade() -> None:
    destination_db_uri = al.context.config.get_main_option('destination_db_uri')
    destination_engine = sa.create_engine(destination_db_uri)
    destination_conn = destination_engine.connect()
    # destination_metadata = sa.MetaData(bind=destination_conn)
    # destination_table = sa.Table('destination_table', destination_metadata, autoload=True)
    # destination_metadata = sa.MetaData()
    # destination_metadata.drop_all(destination_engine, checkfirst=False)

