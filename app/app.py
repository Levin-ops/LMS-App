from models import db, Course
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort
from routes.courses import courses_bp
from routes.instructors import instructor_bp
from routes.students import student_bp
from routes.users import users_bp

app = Flask(__name__)
app.register_blueprint(courses_bp)
app.register_blueprint(instructor_bp)
app.register_blueprint(student_bp)
app.register_blueprint(users_bp)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mach.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


























if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)