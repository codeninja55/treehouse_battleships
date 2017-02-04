import os

# clears the screen based on the esc key being printed
def clear_screen():
    if os.name == 'nt':
        print("\x1b", end=" ")
    else:
        print("\033c", end=" ")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def validate_input(content):
    # TODO - validate user input
    # if user input invalid, rerun the prompt

    # Be as accepting as possible of input. For example, spaces before or
    # after the player’s input is allowed. Both lower and uppercase
    # characters are also allowed. In order to reduce confusion, you may
    # want to clear the screen and display the screen again before each
    # attempt.
    pass