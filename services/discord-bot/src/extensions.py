import discord
from loguru import logger


intents = discord.Intents.all()

logger.add(
    sink="./logs/debug.log",
    format='{time} | {level} : {message}',
    level='DEBUG',
    rotation='20 KB',
    compression='zip'
)