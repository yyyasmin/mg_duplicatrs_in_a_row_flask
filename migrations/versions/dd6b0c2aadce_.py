"""empty message

Revision ID: dd6b0c2aadce
Revises: 
Create Date: 2024-07-16 14:51:55.255970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd6b0c2aadce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'subject', ['subject_id'], ['id'])
        batch_op.drop_column('subject')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('subject_id')

    op.drop_table('subject')
    # ### end Alembic commands ###
