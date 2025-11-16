from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.bookings import (
    BookingCreateData, 
    create_booking, 
    delete_booking, 
    read_all_bookings, 
    read_booking, 
)

# groups of request the server will handle
router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    booking_interface = DBInterface(DBBooking) # create interface
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id:int):
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")
def api_create_booking(booking: BookingCreateData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(booking, booking_interface, room_interface)
Ç

@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id)