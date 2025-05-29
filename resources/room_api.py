from flask_restful import Resource, reqparse
from models.room import Room
from common.db import db

class Room(Resource):
    def get(self):
        room = Room.query.all()
        return [{"id": room.id, "name": room.name, "capacity":room.capacity} for room in room], 200
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('capacity', type=int, required=True, help="This field cannot be left blank")
        
        data = parser.parse_args()
        room = Room.query.filter_by(name=data['name']).first()
        if room:
            return {"message": "Room already exists"}, 400
        new_room = Room(data['name'], data['capacity'])
        db.session.add(new_room)
        db.session.commit()
        return {"message": "Room created successfully"}, 201
    
class RoomDetail(Resource):
    def get(self, room_id):
        room = Room.query.filter_by(id=room_id).first()
        if room:
            return {
                "id": room.id, 
                "name": room.name, 
                "capacity":room.capacity
            }, 200
        else:
            return {"message": "Room not found"}, 404
    def put(self, room_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('capacity', type=int, required=True, help="This field cannot be left blank")
        
        data = parser.parse_args()
        room = Room.query.filter_by(id=room_id).first()
        if room:
            room.name = data['name']
            room.capacity = data['capacity']
            db.session.commit()
            return {"message": "Room updated successfully"}, 200
        else:
            return {"message": "Room not found"}, 404
    def delete(self, room_id):
        room = Room.query.filter_by(id=room_id).first()
        if room:
            db.session.delete(room)
            db.session.commit()
            return {"message": "Room deleted successfully"}, 200
        else:
            return {"message": "Room not found"}, 404