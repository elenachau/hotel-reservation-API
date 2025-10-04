# to access database

from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine: Engine = None # create database engine
DBSession = sessionmaker() # create session to use the database
def init_db(file: str): # hotel.db is sample data here
    engine = create_engine(file)

    # bind Base (in models.py) and session to engine
    Base.metadata.bind = engine
    DBSession.bind = engine