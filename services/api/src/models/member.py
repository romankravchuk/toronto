from sqlalchemy import Column, BigInteger, Integer, String, DateTime

from ..database import Base


class Member(Base):
    __tablename__ = "members"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    discriminator = Column(Integer, nullable=False)
    avatar = Column(String, nullable=False)
    default_avatar = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)