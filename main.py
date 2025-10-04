from dataclasses import dataclass
from datetime import date
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "The server is running"

@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
    email_address: str

@dataclass
class Room:
    id: int
    number: str
    size: int
    price: int

@dataclass
class Booking:
    id: int
    from_date: date
    to_date: date
    customer: Customer
    room: Room
    price: int