from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    photo_url = db.Column(db.String)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(25), nullable = False)
    usertype = db.Column(db.String(25))
    registration_date = db.Column(db.TIMESTAMP)

    student = db.relationship('Student', back_populates='user', uselist=False)
    instructor = db.relationship('Instructor', back_populates='user', uselist=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'photo_url': self.photo_url,
            'email': self.email,
            'usertype': self.usertype,
            'registration_date': self.registration_date,
        }


class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_student_user_id'))
    student_fname = db.Column(db.String(255), nullable=False)
    student_lname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    last_login = db.Column(db.TIMESTAMP)
    usertype = db.Column(db.String(50), nullable=False)
    
    enrollments = db.relationship('Enrollment', back_populates='student')
    grades = db.relationship('Grade', back_populates='student')
    user = db.relationship('User', back_populates='student', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'student_fname': self.student_fname,
            'student_lname': self.student_lname,
            'email': self.email,
            'last_login': self.last_login,
            'usertype': self.usertype,
        }
    


class StudentInstructorAssociation(db.Model):
    __tablename__ = "studentinstructorassociation"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollments.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)



class Instructor(db.Model, SerializerMixin):
    # serialize_rules = ('-courses',)
    __tablename__ = "instructors"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    instructor_fname = db.Column(db.String(255), nullable=False)
    instructor_lname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String)
    bio = db.Column(db.Text)
    experience = db.Column(db.Text)
    specialization = db.Column(db.Text)
    usertype = db.Column(db.String(50))
    
    courses = db.relationship('Course', back_populates='instructor')
    user = db.relationship('User', back_populates = 'instructor', uselist = False)

    def to_dict(self):
        return {
            'id': self.id,
            'instructor_fname': self.instructor_fname,
            'instructor_lname': self.instructor_lname,
            'email': self.email,
            'bio': self.bio,
            'experience': self.experience,
            'specialization': self.specialization,
            'usertype': self.usertype,
        }

class Course(db.Model, SerializerMixin):
    serialize_rules = ('-instructor',)
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))

    enrollments = db.relationship('Enrollment', back_populates='course', lazy='dynamic')
    instructor = db.relationship('Instructor', back_populates='courses')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'instructor_id': self.instructor_id,
        }

class Grade(db.Model):
    __tablename__ = "grades"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollments.id'))
    grade_value = db.Column(db.Text)
    feedback = db.Column(db.Text)
    evaluation_date = db.Column(db.TIMESTAMP)

    student = db.relationship('Student', back_populates='grades')    
    enrollment = db.relationship('Enrollment', back_populates='grade')    


class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    enrollment_date = db.Column(db.TIMESTAMP)
    completion_status = db.Column(db.String(50))

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
    grade = db.relationship('Grade', back_populates='enrollment')