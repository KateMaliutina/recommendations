"""update set is_dynamic false

Revision ID: 6c60f59c85c5
Revises: 463d34bcefa6
Create Date: 2025-06-03 22:00:45.071647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c60f59c85c5'
down_revision: Union[str, None] = '463d34bcefa6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""UPDATE roadmaps SET is_dynamic = FALSE WHERE id < 25;""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""UPDATE roadmaps SET is_dynamic = null WHERE id < 25;""")
