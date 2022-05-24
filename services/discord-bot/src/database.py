from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Settings


engine = create_engine(Settings.CONNECTION_STRING)

Session = sessionmaker(bind=engine)

Base = declarative_base()
