# Security Module

# Imports
from os import getcwd, getenv
from json import loads, dumps
from time import time
from discord.errors import NotFound

from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s
from Core.ID import is_user

# Configure mutes
async def set_mutes(config_path, addition, ctx, args):
    new_mute = args[0]
    
    # Clean up ID
    id_test = is_user(new_mute)
    if not id_test[0]:
        return "Not a valid user"
    else:
        new_mute_id = id_test[1]
    # Try to grab member
        try:
            member = await ctx.guild.fetch_member(new_mute_id)
        # No member is found
        except NotFound:
            log("s", 0, f"{new_mute_id} does not exist in guild {ctx.guild.id}")
            return f"{new_mute} doesn't exist in this server!"
    # Check self
    if str(ctx.author.id) == new_mute_id:
        return "You can't mute or unmute yourself!"
    # Grab channels
    channels = await ctx.guild.fetch_channels()
    # Add mute
    if addition:
        # Try to mute
        for channel in channels:
            await channel.set_permissions(member, send_messages=False)
        # LAR
        log(1, "a", f"muted {member.name} ({member.id})")
        return f"Muted {member.mention}!"
    # Remove mute
    else:
        # Try to mute
        for channel in channels:
            await channel.set_permissions(member, overwrite=None)
        # LAR
        log(1, "a", f"unmuted {member.name} ({member.id})")
        return f"Unmuted {member.mention}!"