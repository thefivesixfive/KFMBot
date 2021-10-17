# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
import dashboard
from os import error, getenv
from discord import Client, Game
from random import randint

from Core.Logger import log
from Core.Commands import check_command
# from Modules.Prefix import get_prefix, set_prefix

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
kfm = Client()

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
    # Split CTX into respect variables
    author = ctx.author
    channel = ctx.channel
    # Check Command
    if check_command("CONFIG", ctx.content, author.id) == False:
        return
    # Send confirm msg
    await channel.send("Nothing is wrong here!")
    

# Trigger Bot
if __name__ == "__main__":
    # Deploy dashboard
    log(1, "s", "run dashboard")
    dashboard.deploy()
    
    # Deploy bot
    log(1, "s", "run bot")
    kfm.run(TOKEN)