"""исправление ошибок

Revision ID: e149f1b55c8d
Revises: ce2fb7f68da3
Create Date: 2024-07-02 20:01:42.615052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e149f1b55c8d'
down_revision: Union[str, None] = 'ce2fb7f68da3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
