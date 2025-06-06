"""make name and grade nullable

Revision ID: 41f7d8f03d02
Revises: 5057b1ec9be6
Create Date: 2025-04-30 21:24:18.594589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41f7d8f03d02'
down_revision: Union[str, None] = '5057b1ec9be6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'grade',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'grade',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
