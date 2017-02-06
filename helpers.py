import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def convert_coord(coord):
    """This helper function converts coordinates such as a1 to index numbers"""
    y = ord(coord[0]) - 97

    if len(coord) > 2:
        x = int(coord[1:]) - 1
    else:
        x = int(coord[1]) - 1

    return x, y


def proceed_confirm():
    while True:
        inp = input("\nPress enter/return when you are ready to proceed > ")
        if inp == "":
            break
        else:
            print("\nThat was not the right key, try again...")
            continue