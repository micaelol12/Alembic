"""primeira

Revision ID: d894a7d27934
Revises: 
Create Date: 2025-07-04 11:40:22.662472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd894a7d27934'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'pessoa',
        sa.Column('id',sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False),
    )
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('pessoa')
