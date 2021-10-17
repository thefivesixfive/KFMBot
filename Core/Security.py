# Security Module

# Imports
from os import getcwd, getenv
from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s

# TODO
# Update to have security codes
# __create_admin
# is_admin
# set_admin

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
def check_admin(config_path, message, author, required_level):
    # If -1 (everyone's command)
    if required_level < 0:
        return True
    # These commands will return false later, because this is the first and final
    # check for any general commands. Other ranked commands need to not worry
    # about including -1, so that's why checking for it returns False later in the code

    # Load up files
    admins = __fetch_admin(config_path)
    # Make sure file is not empty
    if not admins[0] == ['']:
        # check each role in file
        for security_id in admins[0]:
            # split apart id
            admin, level = security_id.split("@")
            # check admin and level
            if admin == str(author.id):
                level = int(level)
                if level <= required_level and level > -1:
                    # Success! Log and return
                    log(1, "s", f"User {author.id} ({author.name}) used {required_level} command")
                    return True

    # Convert author roles to string
    author_roles = []
    for role in author.roles:
        author_roles.append(f"{role.id}")

    # Make sure file not is empty
    if not admins[1] == ['']:
        # check each role in file
        for security_id in admins[1]:
            # split apart id
            role, level = security_id.split("@")
            # check admin and level
            if role in author_roles:
                level = int(level)
                if level <= required_level and level > -1:
                    # Success! Log and return
                    log(1, "s", f"User {author.id} ({author.name}) used {required_level} command")
                    return True

    # Grab arguments
    arguments = message.split(" ")[1:]
    # Try security code
    if len(arguments) > 0:
        # Grab security code
        stored_code = getenv("ADMIN");
        log(1, "s", "got env ADMIN")
        # Compare security code
        if arguments[-1] == stored_code:
            # Log to audit and system
            for location in ["a", "s"]:
                log(1, location, "!!! {author.id} ({author.name}) USED SECURITY CODE !!!")
            # Return success
            return True

def __create_admin(config_path, new_admins):
    # Establish slash (/ or \\)
    S = s()
    # Create base filepath
    file_path = getcwd() + S + config_path + S + "admin_"
    # Convert user admins to string
    new_user_admins = ""
    print(new_admins)
    for admin in new_admins[0]:
        new_user_admins += admin + "\n"
    # Convert role admins to string
    new_role_admins = ""
    for admin in new_admins[1]:
        new_role_admins += admin + "\n"
    # Get admin IDs for both individuals and ranks
    io_out(file_path+"people.kfmconfig", new_user_admins)
    io_out(file_path+"roles.kfmconfig", new_role_admins)

# Set admin rank
def set_admin(config_path, admin, modification):
    # Determine if ID
    if "<@&" in admin:
        admin_type = 1
        entity_type = "role"
    elif "<@" in admin:
        admin_type = 0
        entity_type = ""
    else:
        log(0, "s", "no valid ID found in " + admin)
        return "Not a valid user or role!"
    # Grab current admins
    admins = __fetch_admin(config_path)
    # Clean up ID
    new_admin_id = admin
    for character in "<@!&>":
        new_admin_id = new_admin_id.replace(character, "")
    # Remove admin from list
    if modification == "remove":
        # Check if not in list already
        if not new_admin_id in admins[admin_type]:
            return admin + " is not an admin" + entity_type
        # remove admin
        admins[admin_type].remove(new_admin_id)
        # commit
        __create_admin(config_path, admins)
        log(1, "s", "removed " + entity_type + new_admin_id + " from admins")
        # return
        return "Removed " + admin + " from permitted admins"
    # Admin addition
    else:
        # Check if in list already
        if new_admin_id in admins[admin_type]:
            return admin + " is already an admin" + entity_type
        # add admin
        admins[admin_type].append(new_admin_id)
        # commit
        __create_admin(config_path, admins)
        log(1, "s", "added " + entity_type + new_admin_id + " to admins")
        # return
        return "Added " + admin + " to permitted admins"