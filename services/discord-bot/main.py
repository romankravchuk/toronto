import discord
from discord.ext import tasks
from loguru import logger

from config import Settings
from extensions import intents
from crud import create_member, update_member
from models.member import Member


bot = discord.Client(command_prefix=Settings.PREFIX, intents=intents)


@bot.event
async def on_ready():
    logger.debug(bot.status)
    logger.debug(f'Connected as {bot.user.name}\nID: {bot.user.id}')
    add_members.start()
    update_members.start()


@tasks.loop(hours=1)
async def add_members():
    for guild_id in Settings.GUILDS:
        guild = bot.get_guild(guild_id)
        for m in guild.members:
            member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                            str(m.default_avatar), m.created_at, m.status[0])
            
            if create_member(member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} added')
        


@tasks.loop(minutes=30)
async def update_members():
    for guild_id in Settings.GUILDS:
        guild = bot.get_guild(guild_id)
        for m in guild.members:
            member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                            str(m.default_avatar), m.created_at, m.status[0])
            
            if update_member(id=m.id, member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} updated')


try:
    bot.run(Settings.TOKEN)
except AttributeError as e:
    logger.debug(e)
