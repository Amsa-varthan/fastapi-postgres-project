"""Create user authentication tables

Revision ID: b581bd74a949
Revises: 28095f3a331c
Create Date: 2025-07-22 13:22:10.783496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b581bd74a949'
down_revision: Union[str, Sequence[str], None] = '28095f3a331c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone_verification',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('session_type', sa.Enum('signup', 'login', name='session_type'), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('otp_hash', sa.String(), nullable=False),
    sa.Column('attempts', sa.Integer(), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phone_verification_session_id'), 'phone_verification', ['session_id'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('is_phone_verified', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('is_email_verified', sa.Boolean(), nullable=True),
    sa.Column('address', sa.JSON(), nullable=False),
    sa.Column('account_status', sa.Enum('active', 'suspended', 'deleted', name='account_status'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=True)
    op.create_table('user_tokens',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('refresh_token_hash', sa.String(length=255), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_index(op.f('ix_items_name'), table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('items_pkey'))
    )
    op.create_index(op.f('ix_items_name'), 'items', ['name'], unique=False)
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)
    op.create_index(op.f('ix_items_description'), 'items', ['description'], unique=False)
    op.drop_table('user_tokens')
    op.drop_index(op.f('ix_users_phone'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_phone_verification_session_id'), table_name='phone_verification')
    op.drop_table('phone_verification')
    # ### end Alembic commands ###
