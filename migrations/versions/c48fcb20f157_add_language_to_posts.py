"""add language to posts

Revision ID: c48fcb20f157
Revises: e383cf98fc0f
Create Date: 2020-11-08 13:50:53.389966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c48fcb20f157"
down_revision = "e383cf98fc0f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("post", sa.Column("language", sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("post", "language")
    # ### end Alembic commands ###
