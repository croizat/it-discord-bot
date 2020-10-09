import discord
from discord.ext import commands
import Currency
import LiveMarket


class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def Rates(self, ctx):
        market = LiveMarket.API()
        rates = market.request('USD')

        parsedRates = str()
        currency = Currency.Utility()

        parsedRates += '%s %s is the base currency\n' % (currency.getFlagEmoji('USD'), currency.getFullName('USD'))
        for key in rates:
            flag = currency.getFlagEmoji(key)
            fullname = currency.getFullName(key)
            parsedRates += '%s %s[%s] - %.4f \n' % (flag, fullname, key, rates[key])

        await ctx.send(parsedRates)

    @commands.command()
    async def Convert(self, ctx, *args):
        if 3 <= len(args) <= 4:
            await ctx.send('[amount] [from_currency] [to_currency]')
            return

        fromCurrency = args[1].upper()
        toCurrency = args[2].upper()
        amount = args[-1]

        if not amount.isnumeric():
            await ctx.send("""use numbers, that'd help""")
            return

        amount = float(amount)
        currency = Currency.Utility()

        if not currency.exist(fromCurrency.upper()) or not currency.exist(toCurrency.upper()):
            await ctx.send('lol')
            return

        market = LiveMarket.API()
        rates = market.request(fromCurrency)
        if toCurrency in rates:
            rate = float(rates[toCurrency])
            await ctx.send('%.2f %s to %s = %.2f' % (amount, fromCurrency, toCurrency, rate * amount))


def setup(bot):
    bot.add_cog(Converter(bot))
