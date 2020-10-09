import discord
from discord.ext import commands
import wikipedia

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def wiki(self, ctx, article):
        try:
            embed = discord.Embed()
            embed.add_field(title=article.title(), description=wikipedia.summary(article))
            await channel.send(embed=embed)
        except:
            await channel.send(wikipedia.search(article))


def setup(bot):
    bot.add_cog(Wiki(bot))
