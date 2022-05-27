from discord.ext import commands, tasks

from . import BaseCog
from ..extensions import is_me, logger
from ..models.guild import Guild
from ..models.member import Member
from ..systems.guild import guild_system
from ..systems.member import member_system


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

    @task.command()
    @is_me()
    async def stop_adding_guild(self, ctx):
        if self.add_guilds.is_running():
            self.add_guilds.stop()

    @task.command()
    @is_me()
    async def start_adding_member(self, ctx):
        if not self.add_members.is_running():
            self.add_members.start()

    @task.command()
    @is_me()
    async def stop_adding_member(self, ctx):
        if self.add_members.is_running():
            self.add_members.stop()

    @task.command()
    @is_me()
    async def start_updating_member(self, ctx):
        if not self.update_members.is_running():
            self.update_members.start()

    @task.command()
    @is_me()
    async def stop_updaing_member(self, ctx):
        if self.update_members.is_running():
            self.update_members.stop()

    @tasks.loop(hours=24)
    async def add_guilds(self):
        for g in self.bot.guilds:
            guild = Guild(g.id, g.name, str(g.icon))

            if guild_system.create_guild(guild=guild):
                logger.debug(f'Guild {guild.id} added')
    
    @tasks.loop(hours=1)
    async def add_members(self):
        for guild in self.bot.guilds:
            for m in guild.members:
                member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                                str(m.default_avatar), m.created_at, m.status[0])
                
                if member_system.create_member(member=member):
                    logger.debug(f'Member {member.name}#{member.discriminator} added')
    
    @tasks.loop(minutes=5)
    async def update_members(self):
        for guild in self.bot.guilds:
            for m in guild.members:
                member = Member(m.id, m.name, m.discriminator, str(m.avatar),
                                str(m.default_avatar), m.created_at, m.status[0])
                
                if member_system.update_member(id=m.id, member=member):
                    logger.debug(f'Member {member.name}#{member.discriminator} updated at {member.updated_at.strftime("%m.%d.%Y %H:%M:%S")}')



def setup(client: commands.Bot):
    client.add_cog(Tasks(client))
