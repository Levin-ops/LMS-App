from flask import Blueprint
from flask_restful import reqparse, Api, Resource
from models import Course, db

courses_bp = Blueprint('courses', __name__)

api = Api(courses_bp)

course_parser = reqparse.RequestParser()
course_parser.add_argument('title', type = str, help = 'Course Title Needed')
course_parser.add_argument('description', type = str, help = "Course description required")
course_parser.add_argument('duration', type = str, help = "Duration of course")
course_parser.add_argument("instructor_id", type = int, help = 'Instructor ID required')


class Courses(Resource):
    def get(self):
        courses = Course.query.all()
        response = [course.to_dict() for course in courses]
        return response

    def post(self):
        pass

class CoursesByID(Resource):
    def get(self, id):
        course = Course.query.get(id)
        if course:
            return course.to_dict(), 200
        else:
            return {'message': 'Course not found'}, 404

    def put(self, id):
        course = Course.query.get(id)
        if course:
            args = course_parser.parse_args()
            course.title = args['title']
            course.description = args['description']
            course.duration = args['duration']
            course.instructor_id = args['instructor_id']

            db.session.commit()
            
            return {'message': 'Course updated successfully'}, 200
        else:
            return {'message': 'Course not found'}, 404

    def delete(self, id):
        course = Course.query.get(id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return {'message': 'Course deleted successfully'}, 200
        else:
            return {'message': 'Course not found'}, 404






api.add_resource(Courses, '/courses')
api.add_resource(CoursesByID, '/courses/<int:id>')