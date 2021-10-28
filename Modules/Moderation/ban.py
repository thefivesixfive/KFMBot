# Kick module
from Core.ID import is_user
from Core.IO import log

async def ban(kfm, ctx, arguments):
    # Try to parse ID
    id = is_user(arguments[0])
    # check if author
    if str(ctx.author.id) == id[1]:
        return "You can't ban yourself!"
    # Run command
    try:
        # generate reason
        reason = " ".join(arguments[1:])
        # Grab user and kick
        target = await kfm.fetch_user(id[1])
        await ctx.guild.ban(target, reason=reason)
        # Message and log
        message = f"Banned {target.name}#{target.discriminator} ({target.id}) from the server!"
        log(1, "a", f"Banned user {target.id} ({target.name}#{target.discriminator})")
    except Exception as e:
        message = "Invalid user!"
        log(0, "s", f"Failed to ban {id} for {e}")
    # Return message
    return message

async def unban(kfm, ctx, arguments):
    # Try to parse ID
    id = is_user(f"<@!{arguments[0]}>")
    # check if author
    if str(ctx.author.id) == id[1]:
        return "You can't unban yourself!"
    # Run command
    try:
        # Grab bans
        bans = await ctx.guild.bans()
        users = [ban.user for ban in bans]
        ids = [user.id for user in users]
        # Grab target
        target = await kfm.fetch_user(id[1])
        if target.id in ids:
            await ctx.guild.unban(target)
            # Message and log
            message = f"Unbanned {target.name}#{target.discriminator} from the server!"
            log(1, "a", f"Unbanned user {target.id} ({target.name}#{target.discriminator})")
        else:
            # Message and log
            message = "That user does not exist or has not been banned!"
            log(0, "s", f"Could not find {target.id} in ban list")
    except Exception as e:
        message = "Invalid user!"
        log(0, "s", f"Failed to ban {id} for {e}")
    # Return message
    return message