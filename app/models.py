from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    registration_date = db.Column(db.DateTime, default = datetime.utcnow)

    student = db.relationship('Student', back_populates='user', uselist=False)
    instructor = db.relationship('Instructor', back_populates='user', uselist=False)
    
    def to_dict(self):
        user_dict = {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'photo_url': self.photo_url,
            'email': self.email,
            'usertype': self.usertype,
        }

        if self.registration_date is not None:
            user_dict['registration_date'] = self.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            user_dict['registration_date'] = None

        return user_dict
        
    
    def password_hasher(self, password):
        self.password = generate_password_hash(password)

    def password_unhasher(self, password):
        return check_password_hash(self.password,password)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email = email).first()



class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_student_user_id'))
    student_fname = db.Column(db.String(255), nullable=False)
    student_lname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    last_login = db.Column(db.DateTime, default = datetime.utcnow)
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
            'last_login': self.last_login.strftime('%Y-%m-%d %H:%M:%S'),
            'usertype': self.usertype,
        }
    


class StudentInstructorAssociation(db.Model):
    __tablename__ = "studentinstructorassociation"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollments.id'))
    start_date = db.Column(db.DateTime, default = datetime.utcnow)
    end_date = db.Column(db.DateTime, default = datetime.utcnow)



class Instructor(db.Model, SerializerMixin):
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
    evaluation_date = db.Column(db.DateTime, default = datetime.utcnow)

    student = db.relationship('Student', back_populates='grades')    
    enrollment = db.relationship('Enrollment', back_populates='grade')    

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'enrollment_id': self.enrollment_id,
            'grade_value': self.grade_value,
            'feedback': self.feedback,
            'evaluation_date': self.evaluation_date.strftime('%Y-%m-%d %H:%M:%S'),
        }


class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    enrollment_date = db.Column(db.DateTime, default = datetime.utcnow)
    completion_status = db.Column(db.String(50))

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
    grade = db.relationship('Grade', back_populates='enrollment')