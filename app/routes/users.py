from flask import Blueprint
from flask_restful import reqparse, Api, Resource
from models import User, db

users_bp = Blueprint('users', __name__)

api = Api(users_bp)

user_parser = reqparse.RequestParser()
user_parser.add_argument('firstname', type = str, help = 'firstname required')
user_parser.add_argument('lastname', type = str, help = "lastname required")
user_parser.add_argument('photo_url', type = str, help = "photo url required")
user_parser.add_argument("email", type = str, help = 'email required')
user_parser.add_argument("password", type = str, help= "password required")
user_parser.add_argument("usertype", type = str)

class Users(Resource):
    def get(self):
        users = User.query.all()
        response = [user.to_dict() for user in users]
        return response

    def post(self):
        pass

class UsersByID(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return user.to_dict(), 200
        else:
            return {'message': 'user not found'}, 404

    def put(self, id):
        user = User.query.get(id)
        if user:
            args = user_parser.parse_args()
            user.firstname = args['firstname']
            user.lastname = args['lastname']
            user.photo_url = args['photo_url']
            user.email = args['email']
            user.password =args['password']
            user.usertype = args['usertype']

            db.session.commit()
            
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404






api.add_resource(Users, '/users')
api.add_resource(UsersByID, '/users/<int:id>')