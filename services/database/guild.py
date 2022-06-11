from psycopg2 import ProgrammingError

from logger import logger

from database import BaseSystem
from .models import Member
from .models import Guild


class GuildSystem(BaseSystem):
    def __init__(self) -> None:
        super().__init__()

    def create_guild(self, guild: Guild):
        db_guild = self.session.query(Guild) \
                            .filter_by(id=guild.id).first()
        
        if db_guild:
            logger.debug(f'Guild {db_guild.id} already exists!')
            return False
        
        try:
            self.session.add(guild)
            self.session.commit()
        except ProgrammingError as e:
            logger.error(e)
            return False
        
        return True
    
    def create_member_guild(self, guild_id: int, member_id: int):
        guild : Guild = self.session.query(Guild) \
                            .filter_by(id=guild_id).first()
        member : Member = self.session.query(Member) \
                            .filter_by(id=member_id).first()
        
        if not guild:
            logger.debug(f'Guild {guild_id} doesn\'t exists.')
            return False

        for m in guild.members:
            if m.id == member.id:
                logger.debug(f'Member {member.id} aleady in guild')
                return False

        try:
            guild.members.append(member)
            self.session.commit()
        except ProgrammingError as e:
            logger.error(e)
            return False

        return True
        


guild_system = GuildSystem()
