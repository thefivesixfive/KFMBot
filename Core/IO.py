# Imports
from Core.Logger import log

# Internal command
def __io(filepath:str, mode:str, write_data:str=None):
    # Open file
    try:
        with open(filepath, mode[0]) as file:
            # Pick read or write
            if mode == "read":
                # Orderd so that log actually is after read
                read_data = file.read()
                log(1, "s", "read from "+filepath)
                return read_data
            # Else (write or append)
            else:
                file.write(write_data)
                log(1, "s", mode+" to "+filepath)
                return True
    # FileNotFound Error
    except FileNotFoundError:
        # Create file
        with open(filepath, "w+") as file:
            pass
    # When an error happens
    except Exception as e:
        # Log
        log_message = "failed "+mode+" to "+filepath+" with error: "+e
        log(0, "s", log_message)
        return False

# File In / Out Manager
def io_out(filepath, data):
    status = __io(filepath, "write", data)
    return status

def io_append(filepath, data):
    status = __io(filepath, "append", data)
    return status

def io_in(filepath):
    data = __io(filepath, "read")
    return data
    