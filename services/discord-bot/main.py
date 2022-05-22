import asyncio
import discord
from discord.ext import commands, tasks
from loguru import logger

from crud import create_member, update_member
from config import settings
from models.member import Member


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

def is_me():
    async def predicate(ctx):
        return ctx.author.id in settings['owners']
    return commands.check(predicate)


@bot.command()
async def hello(ctx, user: discord.Member = None):
    if not user:
        user = ctx.message.author

    await ctx.send(f'Hello, {user.mention}!')


@tasks.loop(minutes=5)
async def add_members(lock, ctx):
    async with lock:
        guild = bot.get_guild(ctx.guild.id)
        async for m in guild.fetch_members():
            member = Member(m.id, m.name, m.discriminator, str(m.avatar_url),
                            str(m.default_avatar_url), m.created_at)
                                            
            if create_member(member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} added')


@tasks.loop(minutes=5)
async def update_members(lock, ctx):
    async with lock:
        guild = bot.get_guild(ctx.guild.id)
        async for m in guild.fetch_members():
            member = Member(m.id, m.name, m.discriminator, str(m.avatar_url),
                            str(m.default_avatar_url), m.created_at)

            if update_member(id=m.id, member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} updated')


@update_members.before_loop
async def before_update_members():
    await bot.wait_until_ready()


@bot.command()
@is_me()
async def create(ctx):
    lock = asyncio.Lock()
    bot.loop.create_task(add_members(lock, ctx))


@bot.command()
@is_me()
async def update(ctx):
    lock = asyncio.Lock()
    bot.loop.create_task(update_members(lock, ctx))


try:
    bot.run(settings['token'])
except AttributeError as e:
    logger.debug(e)
