from dataclasses import dataclass
from datetime import date
from fastapi import FastAPI

from hotel.db.engine import DBSession, init_db
from hotel.db.models import DBRoom
from hotel.routers import rooms

app = FastAPI()

# initialize db
DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event(): # open db
    init_db(DB_FILE)

@app.get("/")
def read_root():
    return "The server is running"

app.include_router(rooms.router)