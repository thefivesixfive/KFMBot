# KFM Bot by fivesixfive (https://fivesixfive.dev)
#

# Imports
import logging
from os import getenv
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
    message = ctx.content
    channel = ctx.channel
    # Check if self
    if author == kfm.user:
        return
    # Check prefixes
    prefixes = prefix.get_prefix("CONFIG")
    score = 2
    for stored_prefix in prefixes:
        # Get prefix based on length of stored data
        message_prefix = message[0:len(stored_prefix)]
        if not prefix.check_prefix("CONFIG", message_prefix):
            # Remove likelyhood
            score -= 1
    # check to see if both prefixes failed
    if not score:
        log(0, "s", "preifx not recognized")
        return
    # Find which command it is

# Trigger Bot
if __name__ == "__main__":
    log(1, "s", "run")
    kfm.run(TOKEN)