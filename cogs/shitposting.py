import discord
from discord.ext import commands


class Shitposts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)
        if "cat" in message.content:
            await message.channel.send("cat")


def setup(bot):
    bot.add_cog(Shitposts(bot))
