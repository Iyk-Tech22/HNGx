"""initial db

Revision ID: 02adba6c1151
Revises: 
Create Date: 2023-09-11 18:11:10.613723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02adba6c1151'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###