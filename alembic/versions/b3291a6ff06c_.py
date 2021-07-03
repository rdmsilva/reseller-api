"""empty message

Revision ID: b3291a6ff06c
Revises: 
Create Date: 2021-07-03 09:46:17.947225

"""
from alembic import op
import sqlalchemy as sa


revision = 'b3291a6ff06c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reseller',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('reseller')
