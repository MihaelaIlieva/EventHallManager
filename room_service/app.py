from flask import Flask
from flask_restful import Api
from common.db import db, init_db
from flask_sqlalchemy import SQLAlchemy
from room_service.room_routes import RoomList, RoomDetail
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

init_db(app)
api = Api(app)


    
api.add_resource(RoomList, '/room')
api.add_resource(RoomDetail, '/rooms/<int:room_id>')

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)