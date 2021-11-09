# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
from discord.flags import Intents
import dashboard
from os import error, getenv
from discord import Client, Intents

from Core.Logger import log
from Core.Prefix import check_prefix
from Core.Security import check_admin, set_admin
from Core.Commands import check_command, grab_command
from Core.ID import is_user

from Modules.Misc import coinflip
from Modules.Misc import help
from Modules.Moderation import kick
from Modules.Moderation import ban
from Modules.Moderation import mute

# Grab Token
try:
    # Running on local PC
    from dotenv import load_dotenv
    load_dotenv()
    print(getenv("ADMIN"))
except Exception as e:
    # Running on replit
    print(e)
TOKEN = getenv("TOKEN")
log(1, "s", "got .env TOKEN")

# Create Client
intents = Intents(messages=True, guilds=True)
kfm = Client(intents=intents)

# Initial Boot
@kfm.event
async def on_ready():
    log(1, "s", "connect")

# Message
@kfm.event
async def on_message(ctx):
    # Check if self
    if ctx.author == kfm.user:
        return
    # Other variables
    CONFIG = "CONFIG"
    # Split CTX into respect variables
    author = ctx.author
    channel = ctx.channel
    command = ctx.content.split(" ")[0]
    arguments = ctx.content.split(" ")[1:]

    # Grab prefix
    parsed_command = check_prefix(CONFIG, command)

    # Check Command
    if check_command(parsed_command):
        # Grab data about command
        log(1, "s", f"command {parsed_command} found in commandex")
        command_reqs = grab_command(parsed_command)

        # Check security
        required_level = command_reqs["perm_lvl"]
        arguments = check_admin(CONFIG, arguments, author, required_level)
        if arguments == None:
            log(0, "s", f"insufficient perms for {command}")
            return

        # Check argument count
        arguments_required = command_reqs["args_req"]
        # check if proper amount of arguments exist
        if int(arguments_required) > len(arguments):
            log(0, "s", f"insufficient arg count for {command}")
            return
    # Otherwise, command not found
    else:
        # Check if muted outside of command
        print(mute.check_mute(CONFIG, ctx))
        if mute.check_mute(CONFIG, ctx):
            await ctx.delete()
        # Continue quit
        log(0, "s", f"command {parsed_command} not found in commandex")
        return

    print("\n\n\nTop of the list\n\n\n")

    # Mute Management
    if parsed_command == "user.mute":
        # Attempt
        message = mute.set_mutes(CONFIG, True, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran user.mute")
        return
    if parsed_command == "user.unmute":
        # Attempt
        message = mute.set_mutes(CONFIG, False, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran user.mute")
        return
    # Check if muted once more, inside the context of unmuting yourself
    print(mute.check_mute(CONFIG, ctx))
    if mute.check_mute(CONFIG, ctx):
        await ctx.delete()

    # Help
    if parsed_command == "help":
        # Run
        message = help.help(arguments)
        # Log
        log(1, "s", "ran help command")
        await ctx.channel.send(message)

    # Admin Set
    if parsed_command == "admin.make":
        # Run command
        message = set_admin(CONFIG, True, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran admin.make")
        return    
    # Admin Remove
    if parsed_command == "admin.smite":
        # Run command
        message = set_admin(CONFIG, False, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran admin.smite")
        return

    print("\n\n\nMiddle of the list\n\n\n")

    # User management
    if parsed_command == "user.kick":
        # Try to kick
        message = await kick.kick(kfm, ctx, arguments)
        await ctx.channel.send(message)
        # Send message and quit
        log(1, "s", "ran user.kick")
        return
    if parsed_command == "user.ban":
        # Try to ban
        message = await ban.ban(kfm, ctx, arguments)
        await ctx.channel.send(message)
        # Send message and quit
        log(1, "s", "ran user.ban")
        return
    if parsed_command == "user.unban":
        # Attempt
        message = await ban.unban(kfm, ctx, arguments)
        await ctx.channel.send(message)
        # Send message and quit
        log(1, "s", "ran user.unban")
        return

    # Execute commands accordingly
    if parsed_command == "coinflip":
        # Generate message and send
        message = coinflip.run(arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran coinflip")
        return

    print("\n\n\nBottom of the list\n\n\n")
    

# Trigger Bot
if __name__ == "__main__":
    # Deploy dashboard
    log(1, "s", "run dashboard")
    dashboard.deploy()
    
    # Deploy bot
    log(1, "s", "run bot")
    kfm.run(TOKEN)