# Kick module
from Core.ID import is_user
from Core.IO import log

async def kick(kfm, ctx, arguments):
    # Try to parse ID
    id = is_user(arguments[0])
    # check if author
    if str(ctx.author.id) == id[1]:
        return "You can't kick yourself!"
    # Run command
    try:
        # generate reason
        reason = " ".join(arguments[1:])
        if reason == "":
            reason = "No reason provided!"
        # Grab user and kick
        target = await kfm.fetch_user(id[1])
        await ctx.guild.kick(target, reason=reason)
        # Message and log
        message = f"Kicked {target.name}#{target.discriminator} from the server!"
        log(1, "a", f"Kicked user {target.id} ({target.name}#{target.discriminator})")
    except Exception as e:
        message = "Invalid user!"
        log(0, "s", f"Failed to kick {id} for {e}")
    # Return message
    return message