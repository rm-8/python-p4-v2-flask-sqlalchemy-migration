"""rename address

Revision ID: 03259a523a88
Revises: 3d969748247b
Create Date: 2024-04-04 20:01:57.709533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03259a523a88'
down_revision = '3d969748247b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
   
    # ### end Alembic commands ###
