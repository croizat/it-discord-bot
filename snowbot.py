import discord
import asyncio

from discord.ext import commands
import Currency
import LiveMarket

from itertools import chain
import sys
import os
from platform import python_version

description = '''utility bot'''
bot = commands.Bot(command_prefix='$', case_insensitive=True, description=description)
test_channel_id = '233452818860736512'  # bot testing channel
reminder_channel_id = '753216226595176529'
send_time = '21:30'  # 7:30am Sydney, +10 UTC
send_time_test = '23:50'


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Running python version {python_version()}')
    print('------')


# class BotClient(discord.Client):
from discord.ext import commands
import Currency
import LiveMarket

description = '''utility bot'''
bot = commands.Bot(command_prefix='$', case_insensitive=True, description=description)
test_channel_id = '233452818860736512'  # bot testing channel
reminder_channel_id = '753216226595176529'
send_time = '21:30'  # 7:30am Sydney, +10 UTC
send_time_test = '23:50'


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Running python version {python_version()}')
    print('------')


@bot.command()
async def Rates(ctx):
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


@bot.command()
async def Convert(ctx, *args):
    if len(args) != 3:
        await ctx.send('fucked it up')
        return

    fromCurrency = args[1].upper()
    toCurrency = args[2].upper()
    amount = args[0]

    if not amount.isnumeric():
        await ctx.send('do you think that\'s a fucking number?')
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

@bot.command()
async def thesenate(ctx, *args):

    output = "**Did you ever hear the tragedy of Darth Plagueis the Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic, he could save others from death, but not himself.** \n\nhttps://imgur.com/8KPtRjS"

    await ctx.send(output)

bot.run(os.environ.get('BOT_TOKEN'))
