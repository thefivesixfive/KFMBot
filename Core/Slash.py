from os import name

# Return path slashes based on OS
def s():
    # Windows
    if name == "nt":
        return "\\"
    # Everything else
    else:
        return "/"