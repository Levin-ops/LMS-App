from models import db, Course
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mach.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


class Courses(Resource):
    def get(self):
        courses = Course.query.all()
        response = [course.to_dict() for course in courses]
        return response

    def post(self):
        pass

api.add_resource(Courses, '/courses')























if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)