from datetime import datetime

from ..database import db


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discriminator = db.Column(db.Integer, nullable=False)
    avatar_url = db.Column(db.String, nullable=False)
    default_avatar_url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, id: int, name: str, discriminator: int,
                 avatar_url: str, default_avatar_url: str, created_at: datetime):
        self.id = id
        self.name = name
        self.discriminator = discriminator
        self.avatar_url = avatar_url
        self.default_avatar_url = default_avatar_url
        self.created_at = created_at

    def __repr__(self) -> str:
        return f'<ID: {self.id}, name: {self.name}, discriminator: {self.discriminator}>'
