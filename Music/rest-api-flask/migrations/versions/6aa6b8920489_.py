"""empty message

Revision ID: 6aa6b8920489
Revises: b8f5a8dc2e25
Create Date: 2022-10-05 12:54:29.706706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa6b8920489'
down_revision = 'b8f5a8dc2e25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###
