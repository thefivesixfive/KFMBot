# Logging Module for KFM Bot

# Imports
from time import gmtime, strftime

# Filepaths
SYSTEM_LOGS = "logs/system.kfmlog"
AUDIT_LOGS = "logs/audit.kfmlog"

# Log Command
def log(status:int=0, logfile:str="s", logmsg:str="foo"):
    # Pick filepath
    LOG_PATH = None
    if logfile == "s":
        LOG_PATH = SYSTEM_LOGS
    else:
        LOG_PATH = AUDIT_LOGS
    
    # Get Time
    gmt_timecode = gmtime();
    gmt_timestamp = strftime("%d %b %y, %H:%M:%S", gmt_timecode)

    # Prepare Log
    if status:
        status_code = "[+]"
    else:
        status_code = "[-]"
    log_message =  status_code+" "+gmt_timestamp+" "+logmsg+"\n"

    # Log
    print("Logged to " + LOG_PATH + " at " + gmt_timestamp)
    with open(LOG_PATH, "a+") as file:
        file.write(log_message)

    # Exit
    return True

# Comment that does nothing