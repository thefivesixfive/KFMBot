# Security Module

# Imports
from os import getcwd, getenv
from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s

def __fetch_admin(config_path):
    # Establish slash (/ or \\)
    S = s()
    # Create base filepath
    file_path = getcwd() + S + config_path + S + "admin_"
    # Get admin IDs for both individuals and ranks
    admin_people = io_in(file_path+"people.kfmconfig").split("\n")
    admin_roles = io_in(file_path+"roles.kfmconfig").split("\n")

    return (admin_people, admin_roles)

# Check admin rank
def is_admin(config_path, security_code, author):
    # Check code first
    stored_code = getenv("ADMIN");
    log(1, "s", "got env ADMIN")
    # check if saved code matches given
    if security_code == stored_code:
        # Log to audit and system
        for location in ["a", "s"]:
            log(1, location, "!!! " + str(author.id)  + " (" + author.name + ") USED SECURITY CODE !!!")
        return "code"
    # Load up files
    admins = __fetch_admin(config_path)
    # If NOT individual file empty
    if not admins[0] == ['']:
        # check author id
        if author.id in admins[0]:
            log(1, "s", "admin granted because of id")
            return "user_id"
    # check role
    if not admins[1] == ['']:
        # check author roles
        for role in author.roles:
            # Compare
            if str(role.id) in admins[1]:
                log(1, "s", "admin granted because of role")
                return "role"
    # Otherwise
    log(0, "s", author.id + " (" +author.name+") attempted admin command usage")
    return "invalid"


