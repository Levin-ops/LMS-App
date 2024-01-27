from flask import Blueprint
from flask import jsonify, request, session
from flask_restful import reqparse, Api, Resource
from models import User, db

login_bp = Blueprint('login', __name__)

api = Api(login_bp)

class Login(Resource):
    def get(self):
        pass
    def post(self):
        user = User.query.filter(
            User.email == request.get_json()['email'].first()
        )
        session['user_id'] = user.id

        return jsonify(user.to_dict())
    
class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id) == session.get('user_id')
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'message':'401: Not Authorized'}), 401

class Logout(Resource):
    def get(self):
        session['user_id'] = None
        return jsonify({"Message":"204:No Content"}), 204

api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')