from datetime import datetime
from flask_login import UserMixin

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


class SessionUser(UserMixin, db.Model):
    __tablename__ = 'session_users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password


    def __repr__(self) -> str:
        return "<SessionUser {0}>".format(self.username)
