from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import Config


engine = create_engine(Config.CONNECTION_STRING)
session = sessionmaker(bind=engine)
Base = declarative_base()

class BaseSystem(object):
    def __init__(self) -> None:
        self.session = session()