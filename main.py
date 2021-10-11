# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
import logging
from os import error, getenv
from discord import Client
from dotenv import load_dotenv

from Core.Logger import log
from Modules.Prefix import prefix
# from Modules.Prefix import get_prefix, set_prefix

# Grab Token
load_dotenv()
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
    # Basic help command
    if command == "help":
        # Return message
        await channel.send("Help is W.I.P!")
    # Find which command it is
    if command == "prefix":
        # Attempt to set prefix
        status = prefix.set_prefix("CONFIG", message[1])
        # Return message
        await channel.send(status)
    

# Trigger Bot
if __name__ == "__main__":
    log(1, "s", "run")
    kfm.run(TOKEN)