from ..database import db


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discriminator = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String, nullable=False)
    default_avatar = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self, id, name, discriminator, avatar,
                default_avatar, created_at, status):
        self.id = id
        self.name = name
        self.discriminator = discriminator
        self.avatar = avatar
        self.default_avatar = default_avatar
        self.created_at = created_at
        self.status = status

    def __repr__(self) -> str:
        return f'<ID: {self.id}, name: {self.name}, discriminator: {self.discriminator}>'
