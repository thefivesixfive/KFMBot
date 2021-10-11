# Logging Module for KFM Bot

# Imports
from time import gmtime, strftime
from os import getcwd

# Filepaths
SYSTEM_LOGS = "\\Core\\Logs\\system.kfmlog"
AUDIT_LOGS = "\\Core\\Logs\\audit.kfmlog"

# Log Command
def log(status:int=0, logfile:str="s", logmsg:str="foo"):
    # Pick filepath
    LOG_PATH = None
    if logfile == "a":
        LOG_PATH = AUDIT_LOGS
    else:
        LOG_PATH = SYSTEM_LOGS
    
    # Get Time
    gmt_timecode = gmtime();
    gmt_timestamp = strftime("%d %b %y, %H:%M:%S", gmt_timecode)

    # Prepare Log
    if status:
        status_code = "[+]"
    else:
        status_code = "[-]"
    log_message =  status_code+" "+gmt_timestamp+" "+logmsg

    # Log
    print(log_message)  
    with open(getcwd()+LOG_PATH, "a+") as file:
        file.write(log_message+"\n")

    # Exit
    return True

# Comment that does nothing