from src.bot import bot
from src.config import Settings
from src.extensions import logger


try:
    bot.run(Settings.TOKEN)
except AttributeError as e:
    logger.debug(e)