from discord.ext import commands

from config import BotConfig
from logger import logger
from .extensions import intents


class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(**options)
        self.command_prefix = BotConfig.PREFIX

    def load_cogs(self):
        for cog in BotConfig.COGS:
            self.load_extension(f'bot.cogs.{cog}')
            logger.debug(f'Cog {cog} loaded')

    async def on_ready(self):
        logger.debug(F'Connected as {self.user.name}#{self.user.discriminator}')
        self.load_cogs()


bot = Bot(command_prefix=BotConfig.PREFIX, intents=intents)
