import discord
from discord.ext import tasks

from .config import Settings
from .extensions import intents, logger
from .crud import create_member, update_member
from .models.member import Member


client = discord.Client(command_prefix=Settings.PREFIX, intents=intents)


@client.event
async def on_ready():
    logger.debug(client.status)
    logger.debug(f'Connected as {client.user.name}\nID: {client.user.id}')
    add_members.start()
    update_members.start()


@tasks.loop(hours=1)
async def add_members():
    for guild_id in Settings.GUILDS:
        guild = client.get_guild(guild_id)
        for m in guild.members:
            member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                            str(m.default_avatar), m.created_at, m.status[0])
            
            if create_member(member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} added')
        


@tasks.loop(minutes=30)
async def update_members():
    for guild_id in Settings.GUILDS:
        guild = client.get_guild(guild_id)
        for m in guild.members:
            member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                            str(m.default_avatar), m.created_at, m.status[0])
            
            if update_member(id=m.id, member=member):
                logger.debug(f'Member {member.name}#{member.discriminator} updated')
