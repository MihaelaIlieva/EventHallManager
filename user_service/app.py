from flask import Flask
from flask_restful import Api
from common.db import db
from flask_sqlalchemy import SQLAlchemy
from user_service.user_routes import UserRegister, UserLogin, UserProfile, UserUpdate, UserDelete, UserList, UserSearchByEmail, UserSearchByUsername
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)


with app.app_context():
    db.create_all()

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserProfile, '/user/<int:user_id>')
api.add_resource(UserUpdate, '/user/<int:user_id>/update')
api.add_resource(UserDelete, '/user/<int:user_id>/delete')
api.add_resource(UserList, '/users')
api.add_resource(UserSearchByEmail, '/users/search/email/<string:email>')
api.add_resource(UserSearchByUsername, '/users/search/username/<string:username>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
