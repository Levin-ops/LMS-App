"""table created

Revision ID: c18b9565555a
Revises: 
Create Date: 2024-01-26 17:06:54.258906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c18b9565555a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=25), nullable=True),
    sa.Column('lastname', sa.String(length=25), nullable=True),
    sa.Column('photo_url', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.Column('usertype', sa.String(length=25), nullable=True),
    sa.Column('registration_date', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('instructor_fname', sa.String(length=255), nullable=False),
    sa.Column('instructor_lname', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('experience', sa.Text(), nullable=True),
    sa.Column('specialization', sa.Text(), nullable=True),
    sa.Column('usertype', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('student_fname', sa.String(length=255), nullable=False),
    sa.Column('student_lname', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('last_login', sa.TIMESTAMP(), nullable=True),
    sa.Column('usertype', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_student_user_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('instructor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrollments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('enrollment_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('completion_status', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('enrollment_id', sa.Integer(), nullable=True),
    sa.Column('grade_value', sa.Text(), nullable=True),
    sa.Column('feedback', sa.Text(), nullable=True),
    sa.Column('evaluation_date', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['enrollment_id'], ['enrollments.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('studentinstructorassociation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('instructor_id', sa.Integer(), nullable=True),
    sa.Column('enrollment_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['enrollment_id'], ['enrollments.id'], ),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructors.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studentinstructorassociation')
    op.drop_table('grades')
    op.drop_table('enrollments')
    op.drop_table('courses')
    op.drop_table('students')
    op.drop_table('instructors')
    op.drop_table('users')
    # ### end Alembic commands ###
