# Command Checker

# Imports
from Core.IO import io_in, io_out
from Core.Logger import log
from Core.Prefix import check_prefix
from Core.Security import check_admin
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
def check_command(config_path, message, author):
    print(message)
    # Extract prefixless-command
    command = check_prefix(config_path, message)
    # Grab commandex
    commandex = __open_index()
    # Check if command not in commandex
    if not command in commandex:
        log(0, "s", f"command {command} not found in commandex")
        return (False, False)
    # check if author has perm levels
    required_level = commandex[command]["perm_lvl"]
    message = check_admin(config_path, message, author, required_level)
    print(message)
    if not message:
        log(0, "s", f"insufficient perms for {command}")
        return (False, False)
    # grab required variables
    arguments = message.split(" ")[1:]
    arguments_required = commandex[command]["args_req"]
    # check if proper amount of arguments exist
    if int(arguments_required) > len(arguments):
        log(0, "s", f"insufficient arg count for {command}")
        return (False, False)
    # Everything has passed all checks
    return (command, arguments)