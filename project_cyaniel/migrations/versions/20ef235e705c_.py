"""empty message

Revision ID: 20ef235e705c
Revises: 66a249fe9d40
Create Date: 2017-04-06 22:36:44.491459

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '20ef235e705c'
down_revision = '66a249fe9d40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('character_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_ibfk_2', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'characters', ['character_id'], ['id'])
    op.drop_column('users', 'character')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('character', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_ibfk_2', 'users', 'characters', ['character'], ['id'])
    op.drop_column('users', 'character_id')
    # ### end Alembic commands ###
