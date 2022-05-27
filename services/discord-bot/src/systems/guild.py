from psycopg2 import ProgrammingError

from . import BaseSystem
from ..models.guild import Guild
from ..extensions import logger


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
            logger.debug(e)
            return False
        
        return True


guild_system = GuildSystem()
