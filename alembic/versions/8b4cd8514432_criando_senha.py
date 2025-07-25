"""Criando senha

Revision ID: 8b4cd8514432
Revises: d894a7d27934
Create Date: 2025-07-04 17:26:20.394417

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b4cd8514432'
down_revision: Union[str, Sequence[str], None] = 'd894a7d27934'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa', sa.Column('senha', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa', 'senha')
    # ### end Alembic commands ###
