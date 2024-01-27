from flask import Blueprint
from flask_restful import reqparse, Api, Resource
from models import Instructor, db

instructor_bp = Blueprint('instructors', __name__)

api = Api(instructor_bp)

instructor_parser = reqparse.RequestParser()
instructor_parser.add_argument('firstname', type = str, help = 'Course Title Needed')
instructor_parser.add_argument('lastname', type = str, help = "Course description required")
instructor_parser.add_argument('email', type = str, help = "Duration of course")
instructor_parser.add_argument("bio", type = int, help = 'bio required')
instructor_parser.add_argument("experience", type = int, help = 'experience required')
instructor_parser.add_argument("specialization", type = int, help = 'specialization required')

class Instructors(Resource):
    def get(self):
        instructors = Instructor.query.all()
        response = [instructor.to_dict() for instructor in instructors]
        return response

    def post(self):
        pass

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