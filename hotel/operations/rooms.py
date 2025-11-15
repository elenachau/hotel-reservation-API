from hotel.db.engine import DBSession
from hotel.db.models import DBRoom

def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return rooms

def read_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).get(room_id)
    return room