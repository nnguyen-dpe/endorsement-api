"""empty message

Revision ID: e2a04f030cb1
Revises: 
Create Date: 2018-09-02 01:43:03.171175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2a04f030cb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endorsement',
    sa.Column('developer', sa.String(), nullable=False),
    sa.Column('skill', sa.String(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('developer', 'skill')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endorsement')
    # ### end Alembic commands ###