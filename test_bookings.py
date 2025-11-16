import unittest
from hotel.db.db_interface import DataObject
from hotel.operations.bookings import (
    BookingCreateData,
    InvalidDateError,
    create_booking,
)


class DataInterfaceStub:  # create a stub
    def read_by_id(self, id: int):  # read obj fromn id
        raise NotImplementedError()

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()


class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {
            "id": id,
            "number": "101",
            "size": 10,
            "price": 150_00,
        }  # return stub object


class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)  # create copy
        booking["id"] = 1
        return booking


class TestBooking(unittest.TestCase):
    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2021-12-24", to_date="2021-12-25"
        )
        booking = create_booking(
            data=booking_data,
            booking_interface=BookingInterface(),
            room_interface=RoomInterface(),
        )  # add keyword arguments
        self.assertEqual(booking["price"], 150_00)

    def test_date_error(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2021-12-24", to_date="2021-12-24"
        )
        self.assertRaises(
            InvalidDateError,
            create_booking,
            booking_data,
            BookingInterface(),
            RoomInterface(),
        )


if __name__ == "__main__":
    unittest.main()
