from discord.ext import commands

from .config import Settings
from .extensions import intents, logger


class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(**options)
        self.command_prefix = Settings.PREFIX

    def load_cogs(self):
        for cog in Settings.COGS:
            self.load_extension(f'src.cogs.{cog}')
            logger.debug(f'Cog {cog} loaded')

    async def on_ready(self):
        logger.debug(F'Connected as {self.user.name}#{self.user.discriminator}')
        self.load_cogs()


bot = Bot(command_prefix=Settings.PREFIX, intents=intents)
