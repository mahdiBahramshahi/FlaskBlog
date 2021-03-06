"""empty message

Revision ID: 3657205be196
Revises: 11042095c3a6
Create Date: 2020-10-14 15:31:08.013660

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3657205be196'
down_revision = '11042095c3a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_index('email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('role', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('full_name', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('users')
    # ### end Alembic commands ###
