# Clean up IDs
from re import match
from Core.Logger import log

# Check different types
def is_type(id, qualifier):
    matches = match(f"<({qualifier})([0-9]{18})>", id)
    if matches:
        log(1, "s", f"ID found in {id}")
        return (True, matches.groups()[1])
    else:
        log(0, "s", f"ID not found in {id}")
        return (False, None)
    
def is_user(id):
    return is_type(id, "@!?")

def is_role(id):
    return is_type(id, "@&")

def is_channel(id):
    return is_type(id, "#")

def is_emoji(id):
    return is_type(id, ":.*:")