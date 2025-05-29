from flask_restful import Resource, reqparse
from common.models import Reservation
from common.db import db
from datetime import datetime

reservation_parser = reqparse.RequestParser()
reservation_parser.add_argument('user_id', type=int, required=True,help="User ID is required")
reservation_parser.add_argument('room_id', type=int, required=True,help="Room ID is required")
reservation_parser.add_argument('start_time', type=str, required=True,help="Start time is required")
reservation_parser.add_argument('end_time', type=str, required=True,help="End time is required")

class ReservationListResource(Resource):
    def get(self):
        reservations = Reservation.query.all()
        reservations_list = []
        for reservation in reservations:
            reservations_list.append(reservation.json())
        return reservations_list, 200
    def post(self):
        args = reservation_parser.parse_args()
        try:
            new_reservation = Reservation(user_id=args['user_id'], room_id=args['room_id'], start_time=datetime.fromisoformat(args['start_time']), end_time=datetime.fromisoformat(args['end_time']))
            db.session.add(new_reservation)
            db.session.commit()
            return new_reservation.json(), 201
        except Exception as e:
            return {"message":"An error occurred while creating the reservation", "error": str(e)}, 500
        
class ReservationResource(Resource):
    def get(self, reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            return reservation.json(), 200
        return {"message":"Reservation not found"}, 404
    
    def put(self, reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            args = reservation_parser.parse_args()
            reservation.user_id = args['user_id']
            reservation.room_id = args['room_id']
            reservation.start_time = datetime.fromisoformat(args['start_time'])
            reservation.end_time = datetime.fromisoformat(args['end_time'])

            db.session.commit()
            return {"message":"Reservation updated successfully"}, 200
        return {"message":"Reservation not found"}, 404
    
    def delete(self, reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            db.session.delete(reservation)
            db.session.commit()
            return {"message":"Reservation deleted successfully"}, 200
        return {"message":"Reservation not found"}, 404
            