import discord
from discord.ext import commands
import time


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def start_member_count(self, ctx, channel, *):
        start_time = time.time()
        every_x_seconds = 3600.0
        while True:
            member_count = len([m for m in ctx.guild.members if not m.bot])
            time.sleep(every_x_seconds - ((time.time() - start_time) % every_x_seconds))
            await channel.edit(name=f'Member count: {member_count}')


def setup(bot):
    bot.add_cog(Utilities(bot))
