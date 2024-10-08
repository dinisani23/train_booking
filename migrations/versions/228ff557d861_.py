"""empty message

Revision ID: 228ff557d861
Revises: bcbd98c34a74
Create Date: 2024-09-10 05:10:27.854922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228ff557d861'
down_revision = 'bcbd98c34a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_schedules')
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('train_number',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('customer_email',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'coaches', ['coach_number'], ['coach_number'])
        batch_op.create_foreign_key(None, 'seats', ['seat_number'], ['seat_number'])

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('train_number',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)

    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('train_number',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('origin',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('destination',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(),
               existing_nullable=False)

    with op.batch_alter_table('seats', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('train_number',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'coaches', ['train_number'], ['train_number'])
        batch_op.create_foreign_key(None, 'coaches', ['coach_number'], ['coach_number'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('username',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))
        batch_op.alter_column('email',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('seats', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'coaches', ['train_number', 'coach_number'], ['train_number', 'coach_number'])
        batch_op.alter_column('train_number',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('destination',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('origin',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('train_number',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.alter_column('train_number',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'seats', ['train_number', 'coach_number', 'seat_number'], ['train_number', 'coach_number', 'seat_number'])
        batch_op.create_foreign_key(None, 'coaches', ['train_number', 'coach_number'], ['train_number', 'coach_number'])
        batch_op.alter_column('customer_email',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('train_number',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    op.create_table('_alembic_tmp_schedules',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('train_number', sa.VARCHAR(length=50), nullable=False),
    sa.Column('origin', sa.VARCHAR(length=100), nullable=False),
    sa.Column('destination', sa.VARCHAR(length=100), nullable=False),
    sa.Column('departure_date', sa.DATE(), nullable=False),
    sa.Column('departure_time', sa.TIME(), nullable=False),
    sa.Column('arrival_time', sa.TIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
