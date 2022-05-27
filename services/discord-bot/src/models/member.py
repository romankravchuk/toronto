from datetime import datetime
from sqlalchemy import BigInteger, Integer, Column, ForeignKey
from sqlalchemy import  String, DateTime, Table
from sqlalchemy.orm import relationship, backref

from ..database import Base


member_roles = Table(
    'member_roles',
    Base.metadata,
    Column('role_id', BigInteger, ForeignKey('roles.id'), primary_key=True),
    Column('member_id', BigInteger, ForeignKey('members.id'), primary_key=True),
)


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
    roles = relationship('Role', secondary=member_roles, lazy='subquery',
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
    