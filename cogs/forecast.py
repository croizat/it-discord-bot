import discord
import requests
from discord.ext import commands
import weather


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def weather(self, context, *args):
        if not args:
            forecast = weather.getForecast("victoria, sc")
            embed = discord.Embed(title="Weather Forecast")

            embed.add_field(
                name=forecast.name,
                value="Temperature: "
                + forecast.temperature
                + "\n"
                + "Description: "
                + forecast.description,
                inline=True,
            )

            await context.send(embed=embed)
        else:
            try:
                string = " ".join(args)
                forecast = weather.getForecast(string)
                embed = discord.Embed(title="Weather Forecast")

                embed.add_field(
                    name=forecast.name,
                    value="Temperature: "
                    + forecast.temperature
                    + "\n"
                    + "Description: "
                    + forecast.description,
                    inline=True,
                )

                await context.send(embed=embed)
            except:
                await context.send(
                    """"$weather <city>" dumbfuck. If you did that and it didn't work then the city wasn't count"""
                )


def setup(bot):
    bot.add_cog(Weather(bot))
