from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, DateTime
from database import Base


class Member(Base):
    __tablename__ = "members"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    discriminator = Column(Integer, nullable=False)
    avatar_url = Column(String, nullable=False)
    default_avatar_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

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
