import discord
from discord.ext import commands
from loguru import logger

from .config import Settings


intents = discord.Intents.all()

logger.add(
    sink="./logs/debug.log",
    format='{time} | {level} : {message}',
    level='DEBUG',
    rotation='20 KB',
    compression='zip'
)

def is_me():
    async def predicate(ctx):
        return ctx.author.id in Settings.OWNERS
    return commands.check(predicate)