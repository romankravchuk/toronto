from psycopg2 import ProgrammingError

from logger import logger

from database import BaseSystem
from .models import Member


class MemberSystem(BaseSystem):
    def __init__(self) -> None:
        super().__init__()

    def count(self):
        return self.session.query(Member).count()

    def get_members(self, limit: int, offset: int):
        members = self.session.query(Member) \
                            .limit(limit) \
                            .offset(offset) \
                            .all()
        return members

    def get_member(self, id: int):
        member : Member = self.session.query(Member) \
                            .filter_by(id=id).first()
        
        return member

    def create_member(self, member: Member):
        db_member : Member = self.session.query(Member) \
                        .filter_by(id=member.id).first()
    
        if db_member:
            logger.debug(f'Member {db_member.id} already exists.')
            return False
        
        try:
            self.session.add(member)
            self.session.commit()
        except ProgrammingError:
            return False

        return True
    
    def update_member(self, id: int, member: Member):
        db_member : Member = self.session.query(Member) \
                        .filter_by(id=id).first()
        
        if not db_member:
            logger.debug(f'Member {db_member.id} not exists.')
            return False
        
        try:
            self.session.query(Member).filter(Member.id == id).update({
                Member.avatar : member.avatar,
                Member.name : member.name,
                Member.discriminator : member.discriminator,
                Member.updated_at : member.updated_at
            }, synchronize_session=False)
            self.session.commit()
        except ProgrammingError as e:
            logger.debug(e)
            return False
        
        return True

    def delete(self, id: int):
        member = self.session.query(Member) \
                            .filter_by(id=id) \
                            .first()

        if not member:
            logger.debug(f'Member {id} not exists.')
            return False
        
        try:
            self.session.delete(member)
            self.session.commit()
        except ProgrammingError as e:
            logger.error(e)
            return False
        
        return True

member_system = MemberSystem()
