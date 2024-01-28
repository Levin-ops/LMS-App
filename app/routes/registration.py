from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from models import db, User, Student, Instructor

registration_bp = Blueprint('registration', __name__)
api = Api(registration_bp)

registration_parser = reqparse.RequestParser()
registration_parser.add_argument('firstname', type=str, required=True, help='First name is required')
registration_parser.add_argument('lastname', type=str, required=True, help='Last name is required')
registration_parser.add_argument('email', type=str, required=True, help='Email is required')
registration_parser.add_argument('password', type=str, required=True, help='Password is required')
registration_parser.add_argument('usertype', type=str, required=True, choices=('student', 'instructor'), help='Invalid usertype')
registration_parser.add_argument('bio', type = str)
registration_parser.add_argument('specialization', type= str)


class Registration(Resource):
    def post(self):
        args = registration_parser.parse_args()

        existing_user = User.query.filter_by(email=args['email']).first()
        if existing_user:
            return {'message': 'User with this email already exists'}, 400

        new_user = User(
            firstname=args['firstname'],
            lastname=args['lastname'],
            email=args['email'],
            usertype=args['usertype']
        )
        
        new_user.password_hasher(password = args['password'])

        db.session.add(new_user)
        db.session.commit()

        if args['usertype'] == 'student':
            new_student = Student(
                user=new_user,
                student_fname=args['firstname'],
                student_lname=args['lastname'],
                email=args['email'],
                usertype='student'
            )
            db.session.add(new_student)

        elif args['usertype'] == 'instructor':
            new_instructor = Instructor(
                user=new_user,
                instructor_fname=args['firstname'],
                instructor_lname=args['lastname'],
                email=args['email'],
                usertype='instructor',
                bio=args['bio'],
                specialization=args['specialization']
            )
            db.session.add(new_instructor)

        db.session.commit()

        return {'message': 'User registered successfully', 'user_id': new_user.id}, 201

api.add_resource(Registration, '/register')

