from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from db import db
from models.user import User
from models.room import Room
from models.reservation import Reservation
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# remove this when ready to deploy
with app.app_context():
    db.create_all()

#add logic here

if __name__ == '__main__':
    app.run(debug=True)
