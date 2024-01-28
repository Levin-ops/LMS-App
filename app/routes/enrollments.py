from flask import session, Blueprint
from flask_restful import Resource, reqparse, Api
from models import Student, Enrollment, Course, db
import datetime

enrollment_bp = Blueprint('enrollments', __name__)

api = Api(enrollment_bp)

enrollment_parser = reqparse.RequestParser()
enrollment_parser.add_argument('course_id', type=int, required=True, help='Course ID is required')

class EnrollmentResource(Resource):
    def post(self):
        args = enrollment_parser.parse_args()

        student_email = session.get('user_email')
        student = Student.query.filter_by(email=student_email).first()

        if student:
            course_id = args['course_id']
            course = Course.query.get(course_id)

            if course:
                existing_enrollment = Enrollment.query.filter_by(student_id=student.id, course_id=course_id).first()

                if existing_enrollment:
                    return {'message': 'Student is already enrolled in this course'}, 400

                new_enrollment = Enrollment(
                    student=student,
                    course=course,
                    enrollment_date=datetime.now(),  
                    completion_status='In Progress', 
                )

                db.session.add(new_enrollment)
                db.session.commit()

                return {'message': 'Enrollment successful', 'enrollment_id': new_enrollment.id}, 201
            else:
                return {'message': 'Course not found'}, 404
        else:
            return {'message': 'Student not found'}, 404

api.add_resource(EnrollmentResource, '/enrollments')