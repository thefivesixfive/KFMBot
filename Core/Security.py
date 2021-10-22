# Security Module

# Imports
from os import getcwd, getenv
from json import loads, dumps

from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s
from Core.ID import is_type

# TODO
# Update to have security codes
# __create_admin
# is_admin
# set_admin

def __fetch_admin(config_path):
    # Establish slash (/ or \\)
    S = s()
    # Create base filepath
    file_path = getcwd() + S + config_path + S + "admins.kfmconfig"
    # Get admin IDs for both individuals and ranks
    return loads(io_in(file_path))

# Check admin rank
def check_admin(config_path, arguments, author, required_level):
    # If -1 (everyone's command)
    if required_level < 0:
        return []
    # These commands will return false later, because this is the first and final
    # check for any general commands. Other ranked commands need to not worry
    # about including -1, so that's why checking for it returns False later in the code

    # Try security code
    if len(arguments) > 0:
        # Grab security code
        stored_code = getenv("ADMIN");
        log(1, "s", "got env ADMIN")
        # Compare security code
        if arguments[-1] == stored_code:
            # Log to audit and system
            for location in ["a", "s"]:
                log(1, location, f"!!! {author.id} ({author.name}) USED SECURITY CODE !!!")
            # Return message without security code
            return arguments[:-1]

    # Convert author roles to string
    author_roles = []
    for role in author.roles:
        author_roles.append(f"{role.id}")

    # Load up files
    admins = __fetch_admin(config_path)
    # Make sure file is not empty
    if not admins == "{}":
        # check each role in file
        for id in admins:
            # check admin statement
            is_admin = (id == str(author.id)) or \
                       (id in author_roles)
            if is_admin:
                # Check level
                level = int(admins[id])
                if level <= required_level and level > -1:
                    # Success! Log and return
                    log(1, "s", f"User {author.id} ({author.name}) used {required_level} command (id)")
                    return arguments

    # When all else fails
    return None
            

def __create_admin(config_path, new_admins):
    # Establish slash (/ or \\)
    S = s()
    # Create base filepath
    file_path = getcwd() + S + config_path + S + "admins.kfmconfig"
    # Get admin IDs for both individuals and ranks
    io_out(file_path, dumps(new_admins))

# Set admin rank
def set_admin(config_path, addition, args):
    new_admin = args[0]
    try:
        new_rank = args[1]
    except:
        pass

    # Clean up ID
    id_test = is_type(new_admin, "@!?&?")
    if not id_test[0]:
        return "Not a valid user or role!"
    else:
        new_admin_id = id_test[1]
    # Grab current admins and add new admin
    admins = __fetch_admin(config_path)
    # Make admin
    if addition:
        admins[new_admin_id] = int(new_rank)
        # Write
        __create_admin(config_path, admins)
        # Log and return
        for _ in ["s", "a"]:
            log(1, _, f"added {new_admin} tier {new_rank} admin")
        return f"Gave {new_admin} tier {new_rank} permissions!"
    # Remove admin
    else:
        try:
            admins.pop(new_admin_id)
        # Not an admin
        except:
            return "Not an admin!"
        # Write
        __create_admin(config_path, admins)
        # Log and return
        for _ in ["s", "a"]:
            log(1, _, f"removed {new_admin} as admin")
        return f"Removed {new_admin}'s permissions!"