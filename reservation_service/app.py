from flask import Flask
from flask_restful import Api
from common.db import db, init_db
from flask_sqlalchemy import SQLAlchemy
from reservation_service.reservation_routes import ReservationListResource, ReservationResource
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

init_db(app)
api = Api(app)

    
api.add_resource(ReservationListResource, '/reservations')
api.add_resource(ReservationResource, '/reservations/<int:reservation_id>')

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(port=5002, debug=True)