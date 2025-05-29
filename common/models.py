from common.db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    
class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), unique=True, nullable=False)
    capacity=db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    
class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id=db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    
    user = db.relationship('User', backref='reservations')
    room = db.relationship('Room', backref='reservations')
    
    def __init__(self, user_id, room_id, start_time, end_time):
        self.user_id = user_id
        self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time

