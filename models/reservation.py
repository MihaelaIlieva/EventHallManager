from app import db

class Reservation(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)