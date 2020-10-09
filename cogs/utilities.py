import discord
from discord.ext import commands
import random
import urbandict


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('hi')

    # @commands.command()
    # async def roll(ctx, dice: str):
    #     """Rolls a dice in NdN format."""
    #     try:
    #         rolls, limit = map(int, dice.split('d'))
    #     except Exception:
    #         await ctx.channel.send('Format has to be in NdN!')
    #         return

    #     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    #     await ctx.send(result)

    # @commands.command()
    # async def choose(ctx, *choices: str):
    #     """Chooses between multiple choices."""
    #     await ctx.send(random.choice(choices))

    # @commands.command()
    # async def aesthetify(self, ctx, *, text: str):
    #     """Returns inputed text in aesthetics"""
    #     final = ""
    #     pre = ' '.join(text)
    #     for char in pre:
    #         if not ord(char) in range(33, 127):
    #             final += char
    #             continue
    #         final += chr(ord(char) + 65248)
    #     await self.truncate(ctx.message.channel, final)

    # @commands.command()
    # async def urban(self, ctx, *, word: str):
    #     urb = urbandict.define(word)
    #     if "There aren't any definitions" in urb[0]['def']:
    #         await self.bot.say(":no_mouth: `No definition found.`")
    #         return
    #     msg = "**{0}**\n".format(word)
    #     msg += "`Definition:` {0}\n".format(urb[0]['def'].replace("\n", ""))
    #     msg += "`Example:` {0}".format(urb[0]['example'].replace("\n", ""))
    #     await self.truncate(ctx.message.channel, msg)


def setup(bot):
    bot.add_cog(Utilities(bot))
