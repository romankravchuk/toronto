from src.client import client
from src.config import Settings
from src.extensions import logger


try:
    client.run(Settings.TOKEN)
except AttributeError as e:
    logger.debug(e)