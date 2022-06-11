from loguru import logger

from config import Config


logger.add(
    Config.DEBUG_PATH,
    format=Config.LOG_FORMAT, 
    level=Config.DEBUG, 
    rotation=Config.ROTATION,
    compression=Config.COMPRESSION
)

logger.add(
    Config.ERROR_PATH,
    format=Config.LOG_FORMAT,
    level=Config.ERROR, 
    rotation=Config.ROTATION,
    compression=Config.COMPRESSION
)
