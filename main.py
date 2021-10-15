# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
import dashboard
from os import error, getenv
from discord import Client, Game
from random import randint

from Core.Logger import log
from Modules.Prefix import prefix
from Modules.Security import security
# from Modules.Prefix import get_prefix, set_prefix

# Grab Token
try:
    # Running on local PC
    from dotenv import load_dotenv
    load_dotenv()
except:
    # Running on replit
    pass
TOKEN = getenv("TOKEN")
log(1, "s", "got .env TOKEN")

# Create Client
kfm = Client()

# Initial Boot
@kfm.event
async def on_ready():
    log(1, "s", "connect")
    await kfm.change_presence(activity=Game(name="with deez nuts!"))

# Message
@kfm.event
async def on_message(ctx):
    # Check if self
    if ctx.author == kfm.user:
        return
    # Split CTX into respect variables
    author = ctx.author
    channel = ctx.channel
    # Check prefix
    if prefix.check("CONFIG", ctx.content):
        return
    
    # ARGLESS Commands
    if command == "coinflip":
        # Get random number
        number = randint(0,1)
        # Send heads or tails
        if number:
            await channel.send("Heads!")
        else:
            await channel.send("Tails!")
        return

    # NON-ADMIN COMMANDS (with args)
    args = message[1:]
    if args == []:
        # No args found
        return
    
    # ADMIN COMMANDS
    # If no security code, quit
    method = security.is_admin("CONFIG", args[-1], author)
    if method == "invalid":
        return
    # If security code, trim it
    elif method == "code":
        # Make sure not creating empty list
        if not len(args) < 2:
            args = args[0:-1]
        # Removing code creates empty list
        else:
            await channel.send("Provide more arguments before security code!")
            return

    # Prefix set command
    if command == "prefix":
        # Attempt to set prefix
        status = prefix.set_prefix("CONFIG", args[0])
        await channel.send(status)

    # Admin set command
    if command == "admin+":
        # Attempt to set admin
        status = security.set_admin("CONFIG", args[0], modification="add")
        await channel.send(status)
    
    # Admin remove command
    if command == "admin-":
        # Attempt to set admin
        status = security.set_admin("CONFIG", args[0], modification="remove")
        await channel.send(status)
    

# Trigger Bot
if __name__ == "__main__":
    # Deploy dashboard
    log(1, "s", "run dashboard")
    dashboard.deploy()
    
    # Deploy bot
    log(1, "s", "run bot")
    kfm.run(TOKEN)