from datetime import date
from typing import Optional
from hotel.db.engine import DBSession
from hotel.db.models import DBBooking, DBRoom, to_dict
from pydantic import BaseModel

# create custom exception
class InvalidDateError(Exception):
    pass

class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date


class BookingUpdateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date


def read_all_bookings():
    session = DBSession()
    bookings: list[DBBooking] = session.query(DBBooking).all()
    return [to_dict(b) for b in bookings]


def read_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    return to_dict(booking)


def create_booking(data: BookingCreateData):
    session = DBSession()

    # retrieve the room
    room = session.query(DBRoom).get(data.room_id)

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates.")
    
    booking_dict = data.dict()
    booking_dict["price"] = room.price * days

    booking = DBBooking(**data.dict()) # create booking object, convert data to dict
    session.add(booking)
    session.commit()
    return to_dict(booking) # convert to raw data for API to return

def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id) # retrieve booking
    session.delete(booking)
    session.commit()
    return to_dict(booking)