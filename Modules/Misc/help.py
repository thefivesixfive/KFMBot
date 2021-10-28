# Help module

from Core.Commands import check_command, grab_command, all_commands
from Core.IO import log

# Run command
def help(arguments):
    if len(arguments) == 0:
        # Return all commands
        commands = [f"`{command}`" for command in all_commands()]
        return "\n".join(commands)
    if check_command(arguments[0]):
        # Return help
        command_reqs = grab_command(arguments[0])
        message = f"{command_reqs['help']}\n{command_reqs['usage']}"
        # Return
        log(1, "s", f"Sent help for {arguments[0]}")
        return message
    else:
        # Nothing found
        log(0, "s", f"command {arguments[0]} not found in commandex")
        return f"{arguments[0]} is not a command!"