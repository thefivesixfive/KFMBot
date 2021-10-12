# Security Module

# Imports
from os import getcwd, getenv
from Core.Logger import log
from Core.IO import io_in, io_out
from Core.Slash import s

# Check admin rank
def is_admin(security_code):
    # Check code first
    stored_code = getenv("ADMIN");
    if security_code == stored_code:
        return False

    # Otherwise, check ranking
