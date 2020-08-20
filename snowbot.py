import discord
from discord.ext import commands
import random
import os
from platform import python_version
import csv
import datetime

description = '''utility bot'''
bot = commands.Bot(command_prefix='%', description=description)
BOT_TOKEN = os.environ.get('BOT_TOKEN')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Running python version {python_version()}')
    print('------')


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def members(ctx):
    """Returns number of members in the server, not including bots"""
    await ctx.send(f'member count: {len([m for m in ctx.guild.members if not m.bot])}')


@bot.command()
async def time(ctx, time: str, src_zone: str, dest_zone: str):
    """converts time between given timezones"""
    # get the time given in UTC
    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        utc_time = get_utc_time(timezones)
        converted_time = utc_time

    # get the time difference of the target to UTC
    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        split_time = get_target_time_dif(timezones)
        # split utc time zone to hours and minutes in case of time zones with minutes
        time_dif_h = float(split_time[0])
        time_dif_m = 0
        # check if there was a split before trying to get minutes
        if len(split_time) is 2:
            time_dif_m = float(split_time[1])

        # apply timezone time difference
        converted_time = converted_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)

    def get_utc_time(timezones):
        for row in timezones:
            # check for timezone argument against csv data
            if row[0].lower() == sys.argv[2].lower():
                utc_timezone = row[2]
                utc_time_dif = utc_timezone[3:]
                entered_time = datetime.datetime.strptime(sys.argv[1], '%H.%M')
                # split utc time zone to hours and minutes in case of time zones with minutes
                split_time = utc_time_dif.split('.')
                time_dif_h = 0 - float(split_time[0])
                time_dif_m = 0
                # check if there was a split before trying to get minutes
                if len(split_time) is 2:
                    time_dif_m = float(split_time[1])

                # apply timezone time difference
                utc_time = entered_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)
                return utc_time
        # if it get's here timezone code was wrong
        print('First timezone not found')

    def get_target_time_dif(timezones):
        # check for timezone argument against csv data
        for row in timezones:
            if row[0].lower() == sys.argv[3].lower():
                utc_timezone = row[2]
                utc_time_dif = utc_timezone[3:]
                split_time = utc_time_dif.split('.')
                return split_time
        # if it get's here timezone code was wrong
        print('Second timezone not found')

    await ctx.send(f'{time} {src_zone} is {converted_time} {dest_zone}')


# @bot.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)


# @bot.command(description='For when you wanna settle the score some other way')
# async def choose(ctx, *choices: str):
#     """Chooses between multiple choices."""
#     await ctx.send(random.choice(choices))


# @bot.command()
# async def repeat(ctx, times: int, content='repeating...'):
#     """Repeats a message multiple times."""
#     for i in range(times):
#         await ctx.send(content)


# @bot.command()
# async def joined(ctx, member: discord.Member):
#     """Says when a member joined."""
#     await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


# @bot.group()
# async def cool(ctx):
#     """Says if a user is cool.
#     In reality this just checks if a subcommand is being invoked.
#     """
#     if ctx.invoked_subcommand is None:
#         await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


# @cool.command(name='bot')
# async def _bot(ctx):
#     """Is the bot cool?"""
#     await ctx.send('Yes, the bot is cool.')

bot.run(BOT_TOKEN)
