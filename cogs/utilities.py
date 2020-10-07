def is_admin():
    async def predicate(ctx):
        portables = ctx.bot.get_guild(config['portablesServer'])
        if portables:
            member = portables.get_member(ctx.author.id)
            if member:
                admin_role = portables.get_role(config['adminRole'])
                if admin_role in member.roles:
                    return True
        if ctx.author.guild_permissions.administrator or ctx.author.id == ctx.guild.owner.id or ctx.author.id == config['owner']:
            return True
        raise commands.CommandError(message='Insufficient permissions: `Admin`')
    return commands.check(predicate)
