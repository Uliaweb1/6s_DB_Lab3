"""populate data from csv

Revision ID: 42affc971e8d
Revises: 8f087ec4cb82
Create Date: 2024-03-30 16:49:35.650883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pandas as pd

import main

# revision identifiers, used by Alembic.
revision: str = '42affc971e8d'
down_revision: Union[str, None] = '1798ed378c8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    column_list = []
    column_list.append("country") # Text
    # column_list.append("wind_degree") # Integer
    # column_list.append("wind_kph") # floating point number
    # column_list.append("wind_direction") # enumeration
    column_list.append("last_updated") # Date
    column_list.append("sunrise") # Time
    # wind fields
    column_list.extend(["wind_mph", "wind_kph", "wind_degree", "wind_direction"])

    bind = op.get_bind()
    Session = sa.orm.sessionmaker(bind=bind)
    session = Session()
    df = pd.read_csv("GlobalWeatherRepository.csv")
    for i, row in df.iterrows():
        new_instance = main.MyWeatherRecord(
            country = row["country"],
            wind_mph = row["wind_mph"],
            wind_kph = row["wind_kph"],
            wind_degree = row["wind_degree"],
            wind_direction = row["wind_direction"],
            last_updated = row["last_updated"],
            sunrise = row["sunrise"]
        )
        session.add(new_instance)
    session.commit()
    session.close()

def downgrade() -> None:
    op.execute("DELETE FROM weather")
