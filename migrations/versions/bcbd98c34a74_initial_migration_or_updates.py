"""Initial migration or updates.

Revision ID: bcbd98c34a74
Revises: c4a4ca06378c
Create Date: 2024-09-07 23:19:48.458223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcbd98c34a74'
down_revision = 'c4a4ca06378c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('states')
    op.drop_table('trains')
    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('train_number',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('origin',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('destination',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('username',
               existing_type=sa.TEXT(),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.TEXT(),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.TEXT(),
               type_=sa.String(length=128),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=150),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.alter_column('destination',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('origin',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('train_number',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    op.create_table('trains',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('train_number', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('states',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('state_name', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
