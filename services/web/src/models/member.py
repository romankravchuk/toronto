from datetime import datetime
from ..database import db


member_roles = db.Table('member_roles',
    db.Column('role_id', db.BigInteger, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('member_id', db.BigInteger, db.ForeignKey('members.id'), primary_key=True),
)


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discriminator = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String, nullable=False)
    default_avatar = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    roles = db.relationship('Role', secondary=member_roles, lazy='subquery',
                            backref=db.backref('members', lazy=True))

    def __init__(self, id, name, discriminator, avatar,
                default_avatar, created_at, status):
        self.id = id
        self.name = name
        self.discriminator = discriminator
        self.avatar = avatar
        self.default_avatar = default_avatar
        self.created_at = created_at
        self.status = status
        self.updated_at = datetime.utcnow

    def __repr__(self) -> str:
        return f'<MEMBER: {self.id} {self.name}#{self.discriminator}>'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    guild_id = db.Column(db.BigInteger, db.ForeignKey('guilds.id'))
    