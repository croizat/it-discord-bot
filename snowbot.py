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
async def on_connect():
    print("Bot is connected to discord")

# import cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("[cog] Loaded ", filename)

# error handling whenever the command is not found


@bot.event
async def on_error(event, *args, **kwargs):
    print("[!] Error Caused by:  ", event)
    print(args, kwargs)


@bot.event
async def custom_notify():
    '''
    Function to send custom notifications
    '''
    logging.info('Initializing custom notifications...')
    while True:
        to_notify = []
        deleted = []
        notifications = await Notification.query.gino.all()
        if notifications:
            for notification in notifications:
                guild = self.get_guild(notification.guild_id)
                if not guild:
                    continue
                channel = guild.get_channel(notification.channel_id)
                if not channel:
                    continue
                time = notification.time
                interval = timedelta(seconds=notification.interval)
                if time > datetime.utcnow():
                    continue
                to_notify.append([channel, notification.message])
                if interval.total_seconds() != 0:
                    while time < datetime.utcnow():
                        time += interval
                    await notification.update(time=time).apply()
                else:
                    deleted.append(notification.guild_id)
                    await notification.delete()

            for x in to_notify:
                channel, message = x
                try:
                    await channel.send(message)
                except discord.Forbidden:
                    pass

            if deleted:
                for guild_id in deleted:
                    notifications = await Notification.query.where(Notification.guild_id == guild_id).order_by(Notification.notification_id.asc()).gino.all()
                    if notifications:
                        for i, notification in enumerate(notifications):
                            await notification.update(notification_id=i).apply()
        await asyncio.sleep(30)

bot.run(os.environ.get('BOT_TOKEN'))
