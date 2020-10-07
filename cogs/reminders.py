import discord
from discord.ext import commands
from utilities import is_admin


class Notifications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @is_admin()
    async def addnotification(self, ctx, channel, time, interval, *message):
        '''
        Adds a custom notification. (Admin+)
        Format:
        channel: mention, id, or name
        time (UTC): "DD-MM-YYYY HH:MM", "DD/MM/YYYY HH:MM", "DD-MM HH:MM", "DD/MM HH:MM", HH:MM
        interval: HH:MM, [num][unit]* where unit in {d, h, m}, 0 (one time only notification)
        message: string
        '''
        addCommand()
        await ctx.channel.trigger_typing()

        guild = ctx.guild
        msg = ctx.message

        # Check given channel
        temp = None
        if channel:
            if msg.channel_mentions:
                temp = msg.channel_mentions[0]
            elif is_int(channel):
                temp = guild.get_channel(int(channel))
                if not temp:
                    for c in guild.text_channels:
                        if c.name.upper() == channel.upper():
                            temp = c
                            break
            else:
                for c in guild.text_channels:
                    if c.name.upper() == channel.upper():
                        temp = c
                        break
        if temp:
            channel = temp
        else:
            raise commands.CommandError(message=f'Could not find channel: `{channel}`.')

        # Handle input time
        input_time = time
        time = time.replace('/', '-')
        parts = time.split('-')
        if ' ' in parts[len(parts) - 1]:
            temp = parts[len(parts) - 1]
            parts = parts[:len(parts) - 1]
            for part in temp.split(' '):
                parts.append(part)
        if len(parts) == 1:  # format: HH:MM
            parts = parts[0].split(':')
            if len(parts) != 2:
                await ctx.send(f'Time `{input_time}` was not correctly formatted. For the correct format, please use the `help addnotification` command.')
                return
            hours, minutes = parts[0], parts[1]
            if not is_int(hours):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            hours = int(hours)
            if hours < 0 or hours > 23:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')

            if not is_int(minutes):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            minutes = int(minutes)
            if minutes < 0 or minutes > 59:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            time = datetime.utcnow()
            time = time.replace(microsecond=0, second=0, minute=minutes, hour=hours)
        elif len(parts) == 3:  # format: DD-MM HH:MM
            day = parts[0]
            month = parts[1]
            time_of_day = parts[2]
            if not is_int(month):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            month = int(month)
            if month < 1 or month > 12:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            if not is_int(day):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            day = int(day)
            year = datetime.utcnow().year
            if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif year % 4 == 0 and month == 2 and (day < 0 or day > 29):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif year % 4 != 0 and month == 2 and (day < 0 or day > 28):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            parts = time_of_day.split(':')
            if len(parts) != 2:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            hours, minutes = parts[0], parts[1]
            if not is_int(hours):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            hours = int(hours)
            if hours < 0 or hours > 23:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')

            if not is_int(minutes):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            minutes = int(minutes)
            if minutes < 0 or minutes > 59:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            time = datetime.utcnow()
            time = time.replace(microsecond=0, second=0, minute=minutes, hour=hours, day=day, month=month)
        elif len(parts) == 4:
            day = parts[0]
            month = parts[1]
            year = parts[2]
            time_of_day = parts[3]
            if not is_int(year):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            year = int(year)
            if year < datetime.utcnow().year or year > datetime.utcnow().year + 1:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            if not is_int(month):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            month = int(month)
            if month < 1 or month > 12:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            if not is_int(day):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            day = int(day)
            if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif year % 4 == 0 and month == 2 and (day < 0 or day > 29):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            elif year % 4 != 0 and month == 2 and (day < 0 or day > 28):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            parts = time_of_day.split(':')
            if len(parts) != 2:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            hours, minutes = parts[0], parts[1]
            if not is_int(hours):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            hours = int(hours)
            if hours < 0 or hours > 23:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')

            if not is_int(minutes):
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            minutes = int(minutes)
            if minutes < 0 or minutes > 59:
                raise commands.CommandError(message=f'Invalid argument: `{time}`.')
            time = datetime.utcnow()
            time = time.replace(microsecond=0, second=0, minute=minutes, hour=hours, day=day, month=month, year=year)
        else:
            raise commands.CommandError(message=f'Invalid argument: `{time}`.')
        if time < datetime.utcnow():
            raise commands.CommandError(message=f'Invalid argument: `{time}`.')

        # Handle input time interval
        if interval == '0':
            interval = timedelta(minutes=0)
        elif ':' in interval:  # format: HH:MM
            parts = interval.split(':')
            if len(parts) != 2:
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            hours, minutes = parts[0], parts[1]
            if not is_int(hours):
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            hours = int(hours)
            if hours < 0 or hours > 23:
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')

            if not is_int(minutes):
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            minutes = int(minutes)
            if minutes < 0 or minutes > 59:
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            interval = timedelta(hours=hours, minutes=minutes)
        else:  # format: [num][unit] where unit in {d, h, m}
            temp = interval.replace(' ', '')
            units = ['d', 'h', 'm']
            input = []
            num = ''
            for char in temp:
                if not is_int(char) and not char.lower() in units:
                    raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
                elif is_int(char):
                    num += char
                elif char.lower() in units:
                    if not num:
                        raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
                    input.append((int(num), char.lower()))
                    num = ''
            days = 0
            hours = 0
            minutes = 0
            for i in input:
                num = i[0]
                unit = i[1]
                if unit == 'd':
                    days += num
                elif unit == 'h':
                    hours += num
                elif unit == 'm':
                    minutes += num
            if days * 24 * 60 + hours * 60 + minutes <= 0:
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            elif days * 24 * 60 + hours * 60 + minutes > 60 * 24 * 366:
                raise commands.CommandError(message=f'Invalid argument: `{interval}`.')
            interval = timedelta(days=days, hours=hours, minutes=minutes)

        # Handle input message
        msg = ''
        for m in message:
            msg += m + ' '
        msg = msg.strip()
        if not msg:
            raise commands.CommandError(message=f'Invalid argument: `message`.')

        notifications = await Notification.query.where(Notification.guild_id == ctx.guild.id).order_by(Notification.notification_id.desc()).gino.all()
        id = 0
        if notifications:
            id = notifications[0].notification_id + 1
        await Notification.create(notification_id=id, guild_id=ctx.guild.id, channel_id=channel.id, time=time, interval=interval.total_seconds(), message=msg)

        await ctx.send(f'Notification added with id: `{id}`\n```channel:  {channel.id}\ntime:     {str(time)} UTC\ninterval: {int(interval.total_seconds())} (seconds)\nmessage:  {msg}```')

    @commands.command()
    async def notifications(self, ctx):
        '''
        Returns list of custom notifications for this server.
        '''
        addCommand()

        notifications = await Notification.query.where(Notification.guild_id == ctx.guild.id).order_by(Notification.notification_id.asc()).gino.all()
        if not notifications:
            raise commands.CommandError(message=f'Error: this server does not have any custom notifications.')

        msg = ''
        for notification in notifications:
            msg += f'id:       {notification.notification_id}\nchannel:  {notification.channel_id}\ntime:     {notification.time} UTC\ninterval: {notification.interval} (seconds)\nmessage:  {notification.message}\n\n'
        msg = msg.strip()
        if len(msg) <= 1994:
            await ctx.send(f'```{msg}```')
        else:
            # https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length
            chunks, chunk_size = len(msg), 1994  # msg at most 2000 chars, and we have 6 ` chars
            msgs = [msg[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
            for msg in msgs:
                await ctx.send(f'```{msg}```')

    @commands.command()
    @is_admin()
    async def removenotification(self, ctx, id):
        '''
        Removes a custom notification by ID. (Admin+)
        To get the ID of the notification that you want to remove, use the command "notifications".
        '''
        addCommand()

        if not id:
            raise commands.CommandError(message=f'Required argument missing: `id`.')
        if not is_int(id):
            raise commands.CommandError(message=f'Invalid argument: `{id}`. Must be an integer.')
        else:
            id = int(id)

        notification = await Notification.query.where(Notification.guild_id == ctx.guild.id).where(Notification.notification_id == id).gino.first()
        if not notification:
            raise commands.CommandError(message=f'Could not find custom notification: `{id}`.')

        await notification.delete()

        notifications = await Notification.query.where(Notification.guild_id == ctx.guild.id).order_by(Notification.notification_id.asc()).gino.all()
        if notifications:
            for i, notification in enumerate(notifications):
                await notification.update(notification_id=i).apply()

        await ctx.send(f'Removed custom notification: `{id}`')


def setup(bot):
    bot.add_cog(Notifications(bot))
