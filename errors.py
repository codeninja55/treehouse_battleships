from helpers import clear


class InputError:
    def __init__(self, type, inpt):
        clear()
        print("*" * 60)
        print("You have entered: {}".format(str(inpt).upper()))
        if type == 'index_selection':
            print("Your choice is not available as an index.")
        elif type == 'value':
            print("You have not put an integer number.")
        elif type == 'orientation':
            print("You have not selected a correct value for orientation.")
        elif type == 'coordinates':
            print("You have not put a correct coordinates value number.")
        elif type == 'coordinate_int':
            print("Your coordinates second value is not an integer")
        elif type == 'coordinate_ord':
            print("Your coordinates second value is not a a letter")
        elif type == 'board_boundaries':
            print("Your coordinates are not within the boundaries of the board")
        elif type == 'guess':
            print("Your guess coordinates are invalid.")
        elif type == 'invalid_str':
            print("Your guess coordinates does not start with a letter.")
        elif type == 'guessed_already':
            print("You have already made that guess.")
        elif type == 'confirmation':
            print("You have not made the right selection.")
        print("\nTry again...")
        print("*" * 60)


class ShipPlacementError:
    def __init__(self, type, inpt_coord, inpt_orientation):
        clear()
        print("*" * 60)
        print("You have entered: {}\n"
              "Orientation: {}".format(inpt_coord.upper(),
                                       inpt_orientation.upper()))

        if type == 'outofbounds':
            print("Your placement choice puts the battleship out of bounds of "
              "the board")
        elif type == 'occupied':
            print("These coordinates are occupied by another ship.")
        else:
            print("Unknown Ship Placement Error")

        print("Try again...")
        print("*" * 60)
