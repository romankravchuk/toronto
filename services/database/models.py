from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import (
    Column, 
    BigInteger, 
    String, 
    ForeignKey, 
    Integer, 
    DateTime, 
    Table
)
from sqlalchemy.orm import relationship, backref

from . import Base, engine


_member_roles = Table(
    'member_roles',
    Base.metadata,
    Column('role_id', BigInteger, ForeignKey('roles.id'), primary_key=True),
    Column('member_id', BigInteger, ForeignKey('members.id'), primary_key=True),
)

_guild_members = Table(
    'guild_members',
    Base.metadata,
    Column('guild_id', BigInteger, ForeignKey('guilds.id'), primary_key=True),
    Column('member_id', BigInteger, ForeignKey('members.id'), primary_key=True),
)


class Guild(Base):
    __tablename__ = "guilds"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    icon = Column(String(), nullable=False)
    members = relationship('Member', secondary=_guild_members, lazy='subquery',
                            backref=backref('guilds', lazy=True))    
    roles = relationship('Role', lazy='subquery', backref=backref('guilds', lazy=True))

    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon

    def __repr__(self) -> str:
        return f'<GUILD: {self.id} {self.name}>'

class Member(Base):
    __tablename__ = "members"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    discriminator = Column(Integer, nullable=False)
    avatar = Column(String, nullable=False)
    default_avatar = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    roles = relationship('Role', secondary=_member_roles, lazy='subquery',
                            backref=backref('members', lazy=True))

    def __init__(self, id, name, discriminator, avatar,
                 default_avatar, created_at, status, updated_at = datetime.utcnow()):
        self.id = id
        self.name = name
        self.discriminator = discriminator
        self.avatar = avatar
        self.default_avatar = default_avatar
        self.created_at = created_at
        self.status = status
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f'<ID: {self.id}, name: {self.name}, discriminator: {self.discriminator}>'

class Role(Base):
    __tablename__ = 'roles'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    guild_id = Column(BigInteger, ForeignKey('guilds.id'))
    
    def __init__(self, id, name, guild_id):
        self.id = id
        self.name = name
        self.guild_id = guild_id
    
    def __repr__(self) -> str:
        return f'<ID: {self.id}, name: {self.name}, guild_id: {self.guild_id}>'


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(100), index=True, unique=True, nullable=False)
    password = Column(String(1024), nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password

    def __repr__(self) -> str:
        return f"<User {self.username}>"


if not Base.metadata.tables:
    Base.metadata.create_all(bind=engine)