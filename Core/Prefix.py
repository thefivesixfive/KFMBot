# Prefix module

# Imports
from os import getcwd
from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s

# Get prefix
def get_prefix(config_path):
    # Read file
    file_path = getcwd() + s() + config_path + s() + "prefix.kfm" 
    current_prefix = io_in(file_path+"config")
    static_prefix = io_in(file_path+"static")
    # Return
    return (current_prefix, static_prefix)

# check prefix to see if it matches
def check(config_path, message):
    # Get command from message
    command = message.split(" ")[0]
    # Read prefixes
    prefixes = get_prefix(config_path)
    for prefix in prefixes:
        # check for prefix using splice
        prefix_length = len(prefix)
        if command[0:prefix_length] == prefix:
            print(prefix)
            # Log success
            log(1, "s", "prefix " + prefix + " found in " + command)
            # return success
            return True
    # will only run if both prefixes failed
    return False

# Set prefix
def set_prefix(config_path, new_prefix):
    log(1, "s", "received request to change prefix")
    # Grab current prefixes
    prefixes = get_prefix(config_path)
    # Check if new prefix is static prefix
    if new_prefix == prefixes[1]:
        log(0, "s", "cannot change dynamic prefix to static")
        return "That's already the fallback prefix!"
    # check if new prefix is
    elif new_prefix == prefixes[0]:
        log(0, "s", "dynamic prefix already set to given value")
        return "That's already the current prefix!"
    # check if prefix is too long
    elif len(new_prefix) > 3:
        log(0, "s", "new prefix too long")
        return "That prefix is too long!"
    # otherwise, good to go
    else:
        io_out(getcwd() + s() + config_path + s() + "prefix.kfmconfig", new_prefix)
        log(1, "s", "updated dynamic prefix to " + new_prefix)
        log(1, "a", "updated dynamic prefix to " + new_prefix)
        return "The prefix has been changed to `" + new_prefix + "`"
