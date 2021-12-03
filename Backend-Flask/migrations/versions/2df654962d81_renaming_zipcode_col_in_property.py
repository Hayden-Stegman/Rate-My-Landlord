"""renaming zipcode col in property

Revision ID: 2df654962d81
Revises: 8a4f73f6f4cb
Create Date: 2021-12-03 12:10:25.441598

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2df654962d81'
down_revision = '8a4f73f6f4cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property', sa.Column('zipcode', sa.String(length=5), nullable=True))
    op.drop_column('property', 'zip_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property', sa.Column('zip_code', mysql.VARCHAR(length=5), nullable=True))
    op.drop_column('property', 'zipcode')
    # ### end Alembic commands ###
