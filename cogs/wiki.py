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
            embed = discord.Embed(title=wikipedia.page(article).title, url=wikipedia.page(article).url, description = wikipedia.summary(article))
            await ctx.send(embed = embed)
        except:
            await ctx.send(wikipedia.search(article))


def setup(bot):
    bot.add_cog(Wiki(bot))
