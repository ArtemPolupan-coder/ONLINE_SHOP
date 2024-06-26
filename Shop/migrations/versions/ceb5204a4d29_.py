"""empty message

Revision ID: ceb5204a4d29
Revises: e81bc7f6c6af
Create Date: 2024-06-12 13:58:45.910159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceb5204a4d29'
down_revision = 'e81bc7f6c6af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.TEXT(length=60),
               type_=sa.String(length=60),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.TEXT(), nullable=True))
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=60),
               type_=sa.TEXT(length=60),
               nullable=False)

    # ### end Alembic commands ###
