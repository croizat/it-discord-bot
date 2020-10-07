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


@bot.event
async def on_member_join(member):
    member_counts = len([m for m in ctx.guild.members if not m.bot])
    guild = member.guild
    channel = discord.utils.get(guild.channels, id=763270876606234644)
    await channel.edit(name=f'Members: {guild.member_count}')


@bot.event
async def on_member_remove(member):
    member_counts = len([m for m in ctx.guild.members if not m.bot])
    guild = member.guild
    channel = discord.utils.get(guild.channels, id=763270876606234644)
    await channel.edit(name=f'Members: {guild.member_count}')


@bot.command()
async def refresh_members(ctx):
    member_counts = len([m for m in ctx.guild.members if not m.bot])
    guild = ctx.guild
    channel = discord.utils.get(ctx.guild.channels, id=763270876606234644)
    await channel.edit(name=f'Members: {guild.member_count}')


@bot.command()
async def gmc(ctx):
    member_count = len([m for m in ctx.guild.members if not m.bot])
    await ctx.send(f'members: {member_count}')


@bot.command()
async def tgmc(ctx):
    member_count = len(ctx.guild.members)
    await ctx.send(f'members: {member_count}')


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
