"""team id into nba_standings

Revision ID: fea5090d3836
Revises: 88a71d4f86e7
Create Date: 2024-07-19 17:50:48.724035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fea5090d3836'
down_revision: Union[str, None] = '88a71d4f86e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nba_standings', sa.Column('team_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'nba_standings', ['team_id'])
    op.create_foreign_key(None, 'nba_standings', 'nba_teams', ['team_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'nba_standings', type_='foreignkey')
    op.drop_constraint(None, 'nba_standings', type_='unique')
    op.drop_column('nba_standings', 'team_id')
    # ### end Alembic commands ###
