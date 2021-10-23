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
        log(0, "s", f"command {parsed_command} found in commandex")
        command_reqs = grab_command(parsed_command)
    # Otherwise, command not found
    else:
        log(0, "s", f"command {parsed_command} not found in commandex")
        return
    
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

    # Admin Set
    if parsed_command == "admin.make":
        # Run command
        message = set_admin("CONFIG", True, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran admin.make")
        return
        
    # Admin Remove
    if parsed_command == "admin.smite":
        # Run command
        message = set_admin("CONFIG", False, arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran admin.smite")
        return

    # User management
    if parsed_command == "user.kick":
        # Try to parse ID
        id = is_user(arguments[0])
        # check if author
        if str(ctx.author.id) == id[1]:
            await ctx.channel.send("You can't kick yourself!")
            return
        # Run command
        try:
            # generate reason
            reason = " ".join(arguments[1:])
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
        await ctx.channel.send(message)
        return

    # Execute commands accordingly
    if parsed_command == "coinflip":
        # Generate message and send
        message = coinflip.run(arguments)
        await ctx.channel.send(message)
        # Log and return
        log(1, "s", "ran coinflip")
        return
    

# Trigger Bot
if __name__ == "__main__":
    # Deploy dashboard
    log(1, "s", "run dashboard")
    dashboard.deploy()
    
    # Deploy bot
    log(1, "s", "run bot")
    kfm.run(TOKEN)