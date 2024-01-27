from flask import Blueprint
from flask_restful import reqparse, Api, Resource
from models import Student, db

student_bp = Blueprint('students', __name__)

api = Api(student_bp)

student_parser = reqparse.RequestParser()
student_parser.add_argument('firstname', type = str, help = 'firstname required')
student_parser.add_argument('lastname', type = str, help = "lastname required")
student_parser.add_argument('email', type = str, help = "email required")

class Students(Resource):
    def get(self):
        students = Student.query.all()
        response = [student.to_dict() for student in students]
        return response

    def post(self):
        pass

class StudentsByID(Resource):
    def get(self, id):
        student = Student.query.get(id)
        if student:
            return student.to_dict(), 200
        else:
            return {'message': 'student not found'}, 404

    def put(self, id):
        student = Student.query.get(id)
        if student:
            args = student_parser.parse_args()
            student.student_fname = args['firstname']
            student.student_lname = args['lastname']
            student.email = args['email']

            db.session.commit()
            
            return {'message': 'Student updated successfully'}, 200
        else:
            return {'message': 'Student not found'}, 404

    def delete(self, id):
        student = Student.query.get(id)
        if student:
            db.session.delete(student)
            db.session.commit()
            return {'message': 'Student deleted successfully'}, 200
        else:
            return {'message': 'Student not found'}, 404






api.add_resource(Students, '/students')
api.add_resource(StudentsByID, '/students/<int:id>')