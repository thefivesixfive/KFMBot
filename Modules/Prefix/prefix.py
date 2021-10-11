# Prefix module

# Imports
from os import getcwd
from Core.Logger import log
from Core.IO import io_in, io_out

# Get prefix
def get_prefix(config_path):
    # Read file
    file_path = getcwd() + "\\" + config_path + "\\prefix.kfm" 
    current_prefix = io_in(file_path+"config")
    static_prefix = io_in(file_path+"static")
    # Return
    return (current_prefix, static_prefix)

# check prefix to see if it matches
def check_prefix(config_path, prefix):
    # Read prefixes
    prefixes = get_prefix(config_path)
    # Checks
    if prefix in prefixes:
        return True
    else:
        return False

# Set prefix
def set_prefix(config_path, new_prefix):
    log(1, "s", "received request to change prefix")
    # Grab current prefixes
    prefixes = get_prefix(config_path)
    # Check if new prefix is static prefix
    if new_prefix == prefixes[1]:
        log(0, "s", "cannot change dynamic prefix to static")
        return "static_conflict"
    # check if new prefix is
    elif new_prefix == prefixes[0]:
        log(0, "s", "dynamic prefix already set to given value")
        return "dynamic_conflict"
    # check if prefix is too long
    elif len(new_prefix) > 3:
        log(0, "s", "new prefix too long")
        return "length_oversized"
    # otherwise, good to go
    else:
        io_out(getcwd() + "\\" + config_path + "\\prefix.kfmconfig", new_prefix)
        log(1, "s", "updated dynamic prefix to " + new_prefix)
