"""color added

Revision ID: 3ac35a7fdc71
Revises: e96c9aa8081a
Create Date: 2019-04-25 17:06:18.233773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ac35a7fdc71'
down_revision = 'e96c9aa8081a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('color', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'color')
    # ### end Alembic commands ###
