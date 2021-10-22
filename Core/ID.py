# Clean up IDs
from re import match
from Core.Logger import log

# Check different types
def is_type(id, qualifier):
    # Generate regex to match request ID type of 18 chars
    regex = "<("+qualifier+")([0-9]{18})>"
    matches = match(regex, id)
    # If match found
    if matches:
        # Log and return sucess
        log(1, "s", f"ID found in {id}")
        return (True, matches.groups()[1])
    else:
        # Log and return failure
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