import discord
from discord.ext import commands

from config import BotConfig


intents = discord.Intents.all()


def is_me():
    async def predicate(ctx):
        return ctx.author.id in BotConfig.OWNERS
    return commands.check(predicate)