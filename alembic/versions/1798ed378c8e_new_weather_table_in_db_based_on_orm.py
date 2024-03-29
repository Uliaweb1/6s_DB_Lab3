"""new weather table in db based on orm

Revision ID: 1798ed378c8e
Revises: 
Create Date: 2024-03-29 20:42:23.543316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1798ed378c8e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.Text(), nullable=True),
    sa.Column('wind_mph', sa.DECIMAL(), nullable=True),
    sa.Column('wind_kph', sa.DECIMAL(), nullable=True),
    sa.Column('wind_degree', sa.Integer(), nullable=True),
    sa.Column('wind_direction', sa.Enum('SSE', 'NW', 'W', 'NE', 'SE', 'WNW', 'N', 'NNW', 'E', 'WSW', 'NNE', 'ENE', 'SW', 'S', 'SSW', 'ESE', name='Direction'), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('sunrise', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    # ### end Alembic commands ###
