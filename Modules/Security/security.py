# Security Module

# Imports
from os import getcwd, getenv
from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s

# Check admin rank
def is_admin(security_code, author):
    # Check code first
    stored_code = getenv("ADMIN");
    # check if saved code matches given
    if security_code == stored_code:
        # Log to audit and system
        for location in ["a", "s"]:
            log(1, location, "!!! " + str(author.id)  + " (" + author.name + ") USED SECURITY CODE !!!")
        return True

    # Otherwise, check ranking

