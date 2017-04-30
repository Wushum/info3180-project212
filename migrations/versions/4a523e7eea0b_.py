"""empty message

Revision ID: 4a523e7eea0b
Revises: 
Create Date: 2017-04-30 01:20:12.886922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a523e7eea0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('myprofile',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=8), nullable=True),
    sa.Column('hashed', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('mywish',
    sa.Column('wishid', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('description_url', sa.String(length=500), nullable=True),
    sa.Column('thumbnail_url', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['myprofile.userid'], ),
    sa.PrimaryKeyConstraint('wishid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mywish')
    op.drop_table('myprofile')
    # ### end Alembic commands ###
