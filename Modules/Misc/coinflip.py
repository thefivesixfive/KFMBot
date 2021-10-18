# Return Heads! or Tails! based on a 50/50 pick
from random import choice
def run(args):
    message = ""
    # check for loop count arg
    try:
        iterations = int(args[0])
        # prevent too many
        if iterations > 5:
            message += "You have been limited to 5 flips to prevent spam\n"
            iterations = 5
    except:
        iterations = 1
    # Generate as many flips as needs
    for _ in range(0, iterations):
        # Flip a coin
        message += f"{choice(['Heads!', 'Tails!'])}\n"
    # Return
    return message