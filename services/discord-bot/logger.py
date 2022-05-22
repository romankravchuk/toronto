from loguru import logger


logger.add(
    sink="./logs/debug.log",
    format='{time} | {level} : {message}',
    level='DEBUG',
    rotation='20 KB',
    compression='zip'
)