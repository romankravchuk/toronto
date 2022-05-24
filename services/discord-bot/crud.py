from psycopg2 import ProgrammingError

from database import Session
from models.member import Member
from logger import logger

session = Session()


def create_member(member: Member):
    db_member = session.query(Member) \
                        .filter_by(id=member.id).first()
    
    if db_member:
        logger.debug(db_member)
        return False
    
    try:
        session.add(member)
        session.commit()
    except ProgrammingError:
        return False

    return True


def update_member(id: int, member: Member):
    db_member = session.query(Member) \
                        .filter_by(id=id).first()
    
    if not db_member:
        logger.debug(db_member)
        return False
    
    try:
        session.query(Member).filter(Member.id == id).update({
            Member.avatar : member.avatar,
            Member.name : member.name,
            Member.discriminator : member.discriminator
        }, synchronize_session=False)
    except ProgrammingError:
        return False
    
    return True