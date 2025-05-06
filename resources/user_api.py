from flask_restful import Resource, reqparse
from models.user import User
from db import db

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="Password cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="Email cannot be left blank")

        data = parser.parse_args()
        
        user = User.query.filter_by(username=data['username']).first()
        if user:
            return {'message': 'User already exists'}, 400
        
        new_user = User(data['username'], data['password'], data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201
    
class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="Password cannot be left blank")
        
        data = parser.parse_args()
        
        user = User.query.filter_by(username=data['username']).first()
        if user and user.password == data['password']:
            #can add user info here as well
            return {'message': 'User logged in successfully'}, 200
        else:
            return {'message': 'Invalid username or password'}, 401
        
class UserProfile(Resource):
    
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, 200
        else:
            return {'message': 'User not found'}, 404
        
class UserUpdate(Resource):
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be left blank")
        parser.add_argument('password', type=str, required=False, help="Password cannot be left blank")
        parser.add_argument('email', type=str, required=False, help="Email cannot be left blank")
        
        data = parser.parse_args()
        
        user = User.query.filter_by(id=user_id).first()
        if user:
            if data['password']:
                user.password = data['password']
            if data['email']:
                user.email = data['email']
            db.session.commit()
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404
        
class UserDelete(Resource):
    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404
        
class UserList(Resource):
    def get(self):
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append({
                "id": user.id,
                "username": user.username,
                "email": user.email
            })
        return {'users': user_list}, 200
        
class UserSearchByEmail(Resource):
    def get(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, 200
        else:
            return {'message': 'User not found'}, 404
        
class UserSearchByUsername(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, 200
        else:
            return {'message': 'User not found'}, 404
