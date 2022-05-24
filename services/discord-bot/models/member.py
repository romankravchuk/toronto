from sqlalchemy import Column, BigInteger, Integer, String, DateTime
from database import Base


class Member(Base):
    __tablename__ = "members"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    discriminator = Column(Integer, nullable=False)
    avatar = Column(String, nullable=False)
    default_avatar = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

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
