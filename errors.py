class InputError(Exception):
    pass


class ShipPlacementError:
    # print out error message
    def __init__(self):
        print("\nShip Placement Error")

class CoordinatesOccupiedError:
    def __init__(self):
        print("\nThese coordinates are occupied by another ship")