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
            page = wikipedia.page(article)
        except wikipedia.DisambiguationError:
            disambiguation = True
        except Exception:
            lookup = False

        if page is None and lookup and not disambiguation:
            page = wikipedia.suggest(article)
            await ctx.send(f"Couldn't find {article}. Is {page} right?")
        elif not lookup:
            await ctx.send("OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!")
        else:
            images = page.images
            embed = discord.Embed(title=wikipedia.page(article).title, url=page.url, description=wikipedia.summary(article)) if len(
                images) == 0 else discord.Embed(title=wikipedia.page(article).title, url=page.url, description=wikipedia.summary(article), image=images[0])
            await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
