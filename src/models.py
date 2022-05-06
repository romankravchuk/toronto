from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.date)


    def __init__(self, username, email):
        self.username = username,
        self.email = email


    def __repr__(self) -> str:
        return "<User {0}>".format(self.username)
