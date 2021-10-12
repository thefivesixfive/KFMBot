# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
import dashboard
from os import error, getenv
from discord import Client

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

# Message
@kfm.event
async def on_message(ctx):
    # Split CTX into respect variables
    author = ctx.author
    message = ctx.content.split(" ")
    first_word = message[0]
    channel = ctx.channel
    # Check if self
    if author == kfm.user:
        return
    # Check prefix
    command = prefix.check("CONFIG", first_word)
    if command == first_word:
        return
    # Check for 0 args
    args = message[1:]
    if args == []:
        # No args found
        return
    # NON-ADMIN COMMANDS
    
    
    # ADMIN COMMANDS
    # If no security code, quit
    if not security.is_admin(args[-1], author):
        return
    # If security code, trim it
    else:
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
    

# Trigger Bot
if __name__ == "__main__":
    log(1, "s", "run dashboard")
    dashboard.deploy()
    
    log(1, "s", "run bot")
    kfm.run(TOKEN)