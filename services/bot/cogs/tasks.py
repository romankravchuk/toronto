from discord.ext import commands, tasks

from . import BaseCog
from ..extensions import is_me
from logger import logger
from database.models import Member
from database.models import Guild
from database.models import Role
from database import (
    guild as guil,
    member as mem,
    role as rol
)


class Tasks(BaseCog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__(bot)

    @commands.group(alias=['task'])
    async def task(self, ctx):
        if not ctx.invoked_subcommand:
            if len(ctx.message.role_mentions) != 1:
                return await ctx.send('There is tasks')

    @task.command()
    @is_me()
    async def start_adding_guild(self, ctx):
        if not self.add_guilds.is_running():
            self.add_guilds.start()
            logger.debug('start adding guilds')

    @task.command()
    @is_me()
    async def stop_adding_guild(self, ctx):
        if self.add_guilds.is_running():
            self.add_guilds.stop()
            logger.debug('stop adding guilds')

    @task.command()
    @is_me()
    async def start_adding_member(self, ctx):
        if not self.add_members.is_running():
            self.add_members.start()
            logger.debug('start adding members')

    @task.command()
    @is_me()
    async def stop_adding_member(self, ctx):
        if self.add_members.is_running():
            self.add_members.stop()
            logger.debug('stop adding members')

    @task.command()
    @is_me()
    async def start_updating_member(self, ctx):
        if not self.update_members.is_running():
            self.update_members.start()
            logger.debug('start updating members')

    @task.command()
    @is_me()
    async def stop_updaing_member(self, ctx):
        if self.update_members.is_running():
            self.update_members.stop()
            logger.debug('start updating members')

    @task.command()
    @is_me()
    async def start_adding_roles(self, ctx):
        if not self.create_members_roles.is_running():
            self.create_members_roles.start()
            logger.debug('start adding roles')
    
    @task.command()
    @is_me()
    async def stop_adding_roles(self, ctx):
        if self.create_members_roles.is_running():
            self.create_members_roles.stop()
            logger.debug('stop adding roles')

    @task.command()
    @is_me()
    async def start_updating_roles(self, ctx):
        if not self.update_members_roles.is_running():
            self.update_members_roles.start()
            logger.debug('start updating roles')

    @task.command()
    @is_me()
    async def stop_updating_roles(self, ctx):
        if self.update_members_roles.is_running():
            self.update_members_roles.stop()
            logger.debug('stop updating roles')

    @task.command()
    @is_me()
    async def start_adding_guild_members(self, ctx):
        if not self.create_guild_members.is_running():
            self.create_guild_members.start()
            logger.debug('start adding guild members')

    @task.command()
    @is_me()
    async def stop_adding_guild_members(self, ctx):
        if self.create_guild_members.is_running():
            self.create_guild_members.stop()
            logger.debug('stop adding guild members')

    @tasks.loop(hours=24)
    async def add_guilds(self):
        for g in self.bot.guilds:
            guild = Guild(g.id, g.name, str(g.icon))
            guil.guild_system.create_guild(guild=guild)
    
    @tasks.loop(hours=24)
    async def add_members(self):
        for guild in self.bot.guilds:
            for member in guild.members:
                m = Member(
                    member.id, member.name, member.discriminator, 
                    str(member.avatar), str(member.default_avatar), 
                    member.created_at, member.status[0]
                )
                mem.member_system.create_member(member=m, guild_id=guild.id)
    
    @tasks.loop(minutes=5)
    async def update_members(self):
        for guild in self.bot.guilds:
            for m in guild.members:
                member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                                str(m.default_avatar), m.created_at, m.status[0])
                mem.member_system.update_member(id=m.id, member=member)

    @tasks.loop(hours=24)
    async def create_members_roles(self):
        for guild in self.bot.guilds:
            for role in guild.roles:
                r = Role(role.id, role.name, guild.id)
                rol.role_system.create_role(role=r)
    
    @tasks.loop(minutes=10)
    async def update_members_roles(self):
        for guild in self.bot.guilds:
            for role in guild.roles:
                r = Role(role.id, role.name, guild.id)
                rol.role_system.update_role(role=r)

    @tasks.loop(hours=24)
    async def create_guild_members(self):
        for guild in self.bot.guilds:
            for member in guild.members:
                guil.guild_system.create_member_guild(guild_id=guild.id, member_id=member.id)


def setup(client: commands.Bot):
    client.add_cog(Tasks(client))
