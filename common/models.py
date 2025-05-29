from common.db import db

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
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    
    user = db.relationship('User')
    room = db.relationship('Room')
    
    def __init__(self, user_id, room_id, date, start_time, end_time):
        self.user_id = user_id
        self.room_id = room_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

