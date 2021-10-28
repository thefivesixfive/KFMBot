# Command Checker

# Imports
from Core.IO import io_in, io_out
from Core.Logger import log
from Core.Prefix import check_prefix
from Core.Security import check_admin
from Core.Slash import s

from os import getcwd
from json import load

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
def check_command(command):
    # Grab commandex
    commandex = __open_index()
    # Check if command not in commandex
    return command in commandex

# Grab command data
def grab_command(command):
    # Grab commandex
    commandex = __open_index()
    # Grab data
    return commandex[command]

# All commands
def all_commands():
    # Grab commandex
    commandex = __open_index()
    # Return
    return commandex