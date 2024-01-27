from flask import Blueprint
from flask_restful import reqparse, Api, Resource
from models import Instructor, db

instructor_bp = Blueprint('instructors', __name__)

api = Api(instructor_bp)

instructor_parser = reqparse.RequestParser()
instructor_parser.add_argument('firstname', type = str, help = 'first name required')
instructor_parser.add_argument('lastname', type = str, help = "last name required")
instructor_parser.add_argument('email', type = str, help = "email required")
instructor_parser.add_argument("bio", type = str, help = 'bio required')
instructor_parser.add_argument("experience", type = str, help = 'experience required')
instructor_parser.add_argument("specialization", type = str, help = 'specialization required')

class Instructors(Resource):
    def get(self):
        instructors = Instructor.query.all()
        response = [instructor.to_dict() for instructor in instructors]
        return response

    def post(self):
        args = instructor_parser.parse_args()


        existing_instructor = Instructor.query.filter_by(email=args['email']).first()
        if existing_instructor:
            return {'message': 'Email address is already in use as an Instructor'}, 400
        new_instructor = Instructor(
            instructor_fname=args['firstname'],
            instructor_lname=args['lastname'],
            email=args['email'],
            bio=args['bio'],
            experience=args['experience'],
            specialization=args['specialization']
        )

        db.session.add(new_instructor)
        db.session.commit()

        return {'message': 'Instructor added successfully'}, 201

class InstructorByID(Resource):
    def get(self, id):
        instructor = Instructor.query.get(id)
        if instructor:
            return instructor.to_dict(), 200
        else:
            return {'message': 'Instructor not found'}, 404

    def put(self, id):
        instructor = Instructor.query.get(id)
        if instructor:
            args = instructor_parser.parse_args()
            instructor.instructor_fname = args['firstname']
            instructor.instructor_lname = args['lastname']
            instructor.email = args['email']
            instructor.bio = args['bio']
            instructor.experience = args['experience']
            instructor.specialization = args['specialization']

            db.session.commit()
            
            return {'message': 'Instructor updated successfully'}, 200
        else:
            return {'message': 'Instructor not found'}, 404

    def delete(self, id):
        instructor = Instructor.query.get(id)
        if instructor:
            db.session.delete(instructor)
            db.session.commit()
            return {'message': 'Instructor deleted successfully'}, 200
        else:
            return {'message': 'Instructor not found'}, 404






api.add_resource(Instructors, '/instructors')
api.add_resource(InstructorByID, '/instructors/<int:id>')