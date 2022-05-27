from sqlalchemy import BigInteger, String, Column
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from ..database import Base


guild_members = Table(
    'guild_members',
    Base.metadata,
    Column('guild_id', BigInteger, ForeignKey('guilds.id'), primary_key=True),
    Column('member_id', BigInteger, ForeignKey('members.id'), primary_key=True),
)

guild_roles = Table(
    'guild_roles',
    Base.metadata,
    Column('role_id', BigInteger, ForeignKey('roles.id'), primary_key=True),
    Column('guild_id', BigInteger, ForeignKey('guilds.id'), primary_key=True),
)


class Guild(Base):
    __tablename__ = "guilds"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    icon = Column(String(), nullable=False)
    members = relationship('Member', secondary=guild_members, lazy='subquery',
                            backref=backref('guilds', lazy=True))    
    roles = relationship('Role', secondary=guild_roles, lazy='subquery',
                            backref=backref('guilds', lazy=True))

    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon

    def __repr__(self) -> str:
        return f'<GUILD: {self.id} {self.name}>'