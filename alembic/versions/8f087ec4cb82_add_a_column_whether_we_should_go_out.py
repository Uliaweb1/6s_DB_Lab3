"""add a column whether we should go out

Revision ID: 8f087ec4cb82
Revises: 1798ed378c8e
Create Date: 2024-03-30 16:05:47.735275

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f087ec4cb82'
down_revision: Union[str, None] = '42affc971e8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('weather', sa.Column('should_go_out', sa.Boolean))
    op.execute("UPDATE weather SET should_go_out = (wind_kph > 3.6)")

def downgrade() -> None:
    op.drop_column('weather', 'should_go_out')
