from models import db
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from routes.courses import courses_bp
from routes.instructors import instructor_bp
from routes.students import student_bp
from routes.users import users_bp
from routes.login import login_bp
from routes.registration import registration_bp
from routes.enrollments import enrollment_bp
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mach.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"]= '079af7a11f8b270b9849e05d'
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# JWT_SECRET_KEY = 
jwt = JWTManager()
jwt.init_app(app)



app.register_blueprint(courses_bp)
app.register_blueprint(instructor_bp)
app.register_blueprint(student_bp)
app.register_blueprint(users_bp)
app.register_blueprint(login_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(enrollment_bp)








if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)