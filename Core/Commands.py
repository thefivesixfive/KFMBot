# Command Checker

# Imports
from Core.IO import io_in, io_out
from Core.Logger import log
from Core.Prefix import check_prefix
from Core.Slash import s

from os import getcwd
from json import load, dump

# Load Commandex
def __open_index():
    # Get slash
    S = s()
    # Set filepath
    filepath = f"{getcwd()}{S}Core{S}Commandex{S}commands.json"
    # Read Index
    with open(filepath, "r") as file:
        index = load(file)
    # Return index
    return index

# Check Command
def check_command(config_path, message, author_id):
    # Extract prefixless-command
    command = check_prefix(config_path, message)
    # Grab commandex
    commandex = __open_index()
    # Check if command not in commandex
    if not command in commandex:
        log(0, "s", f"command {command} not found in commandex")
        return False
    # check if author has perm levels
    has_perms = True
    if not has_perms:
        log(0, "s", f"insufficient perms for {command}")
        return False
    # check if proper amount of arguments exist
    arguments = message.split(" ")[1:]
    if commandex[command]["args_req"] < len(arguments):
        return False
    # Everything has passed all checks
    return arguments