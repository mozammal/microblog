"""empty message

Revision ID: f0be157603ea
Revises: c48fcb20f157
Create Date: 2020-11-09 12:54:10.887104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f0be157603ea"
down_revision = "c48fcb20f157"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.Text(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.Column("post_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_comment_timestamp"), "comment", ["timestamp"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_comment_timestamp"), table_name="comment")
    op.drop_table("comment")
    # ### end Alembic commands ###
