import discord
import asyncio
from discord.ext import commands

from itertools import chain
import sys
import os
from platform import python_version

description = '''random utilities and shitposting bot'''
bot = commands.Bot(command_prefix='$', case_insensitive=True, description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Running python version {python_version()}')
    print('------')
    await bot.change_presence(activity=discord.CustomActivity(name="coping"))
    c_total = bot.get_channel(763270876606234644)
    member_count = len([m for m in ctx.guild.members if not m.bot])
    await c_total.edit(name=f'Members: {member_count}')


@bot.event
async def on_connect():
    print("Bot is connected to discord")

# import cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("[cog] Loaded ", filename)


@bot.event
async def on_error(event, *args, **kwargs):
    # error handling whenever the command is not found
    print("[!] Error Caused by:  ", event)
    print(args, kwargs)


bot.run(os.environ.get('BOT_TOKEN'))
