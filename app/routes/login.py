from flask import Blueprint, jsonify, request, session
from flask_restful import  Api, Resource
from models import User, db
from flask_cors import CORS
from flask_jwt_extended import create_access_token, create_refresh_token


login_bp = Blueprint('login', __name__)
CORS(login_bp)
api = Api(login_bp)

class Login(Resource):
    def post(self):
        data = request.get_json()

        user = User.get_user_by_email(email = data.get('email'))

        if user:
            
            access_token = create_access_token(identity= user.email)
            refresh_token = create_refresh_token(identity= user.email)
            
            return {
                    "message": "Logged in",
                    "tokens": {
                        "access_token":access_token,
                        "refresh_token": refresh_token
                    }
                }, 200

        return  {"error":"invalid email or password"}, 400
        

class CheckSession(Resource):
    def get(self):
        try:
            user_id = session.get('user_id')

            if user_id:
                user = User.query.get(user_id)

                if user:
                    return {'message': 'User session found', 'user': user.to_dict()}
                
                else:
                    return {'message': 'User not found'}, 404
            else:
                return {'message': 'User session not found'}, 401

        except Exception as e:
            return {'message': 'An error occurred', 'error': str(e)}, 500

class Logout(Resource):
    def get(self):
        try:
            session['user_id'] = None

            return {"message": "Logout successful"}, 200

        except Exception as e:
            return {'message': 'An error occurred', 'error': str(e)}, 500

api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
