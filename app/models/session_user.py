from flask_login import UserMixin

from ..database import db


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
