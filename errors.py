from helpers import clear


class InputError:
    def index_selection(self):
        clear()
        print("*" * 60)
        print("Your choice is not available as an index.")
        print("Try again...")
        print("*" * 60)

    def value(self):
        clear()
        print("*" * 60)
        print("You have not put an integer number.")
        print("Try again...")
        print("*" * 60)

    def coordinates(self):
        clear()
        print("*" * 60)
        print("You have not put a correct coordinates value number.")
        print("e.g. a1 or a10")
        print("Try again...")
        print("*" * 60)

    def confirmation(self):
        clear()
        print("*" * 60)
        print("You have not made the right selection.")
        print("Try again...")
        print("*" * 60)

class ShipPlacementError:
    # print out error message
    def __init__(self):
        clear()
        print("*" * 100)
        print("Your placement choice puts the battleship out of bounds of "
              "the board")
        print("Try again...")
        print("*" * 100)


class CoordinatesOccupiedError:
    def __init__(self):
        clear()
        print("*" * 60)
        print("These coordinates are occupied by another ship.")
        print("Try again...")
        print("*" * 60)
