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

    output = "**Did you ever hear the tragedy of Darth Plagueis the Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic, he could save others from death, but not himself.** \n\nhttps://imgur.com/8KPtRjS.png"

    await ctx.send(output)


@bot.command()
async def alpha(ctx, *args):

    output = "I am the ultimate alpha male. I only climax for 1 of 2 reasons. I either climax for the purpose of reproduction with a beautiful woman (because that's the only kind of woman worthy of me) or I climax for the purpose of free protein. I need immense protein to maintain my ultimate alpha male body, and 4-5 cum loads a day is sufficient for me. It's not gay if it's mine, but I wouldn't expect you pathetic beta males to understand. I bet you waste your seed into napkins, tissue, and tube socks. How sad, wasting all that protein. Wasting all those offspring. Its optimal for me to masturbate with my legs over my head so I can practice stretching before my workout while I obtain my protein. All the gym betas in the locker room just look away in disgust, but again, I wouldn't be offended by an asshole who only focus on vanity muscles. You beta losers better start acting like real men."

    await ctx.send(output)


@bot.event
async def on_message(message):
    if message.author == client.user:  # Stopping the bot from reading its on message
        return None

    output = "Based? Based on what? In your dick? Please shut the fuck up and use words properly you fuckin troglodyte, do you think God gave us a freedom of speech just to spew random words that have no meaning that doesn't even correllate to the topic of the conversation? Like please you always complain about why no one talks to you or no one expresses their opinions on you because you're always spewing random shit like poggers based cringe and when you try to explain what it is and you just say that it's funny like what? What the fuck is funny about that do you think you'll just become a stand-up comedian that will get a standing ovation just because you said \"cum\" in the stage? HELL NO YOU FUCKIN IDIOT, so please shut the fuck up and use words properly you dumb bitch"

    if "based" in message.content:
        await message.channel.send(output)


@bot.command()
async def meow(ctx, *args):

    output = """leash and treated like a domestic animal then that’s called a fetish, not “quirky” or “cute”. What part of you seriously thinks that any part of acting like a feline establishes a reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to resort to shitty representations of cats to create an illusion of meaning in your worthless life? Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution to your false sense of personality, such as intelligence or charisma in any form or shape. Where do you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely sympathetic towards you as your only escape from the worthless thing you call your existence is to pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant trait, mainly because personality traits require an initial personality to lay their foundation on. You’re not worthy of anybody’s time, so go fuck off, “cat-girl”."""

    await ctx.send(output)


@bot.command()
async def weed(ctx, *args):

    output = """h-hewwo...owunce of weed pwease >///< arigato... dealer-kun puts weedie-chan in bong and inhales waaah!! (╯✧▽✧)╯ daisuki cannabis desu~! (^ ω ^ )uwaaa! weedie-chan i feel so kimochi!!(〃°ω°〃)"""

    await ctx.send(output)


@bot.command()
async def gamer(ctx, *args):

    output = """So the other day, I was playing rainbow six siege, and I heard one of my teammates make a callout in the voice chat. It was a real life gamer girl. God, I kid you not, I just stopped playing and pulled my dick out. “fuck, Fuck!” I was yelling in voice chat. I just wanted to hear her voice again. “Please,” I moaned. But she left the lobby. I was crying and covered in my own cum, but I remembered that I could find recent teammates in the ubiplay friends tab. I frantically closed down siege and opened the tab, to find out she had TTV IN HER NAME!!! She was streaming, and only had 100 viewers!!! The competition was low, so I made the first move and donated my months rent to her. I was already about to pre. She read my donation in the chat. God this is the happiest I’ve been in a long time. I did a little research, and found out where she goes to school, but I am a little nervous to talk to her in person, and need support. Any advice before my Uber gets to her middle school?"""

    await ctx.send(output)

# @bot.command()
# async def name(ctx, *args):

#     output = """"""

#     await ctx.send(output)

bot.run(os.environ.get('BOT_TOKEN'))
