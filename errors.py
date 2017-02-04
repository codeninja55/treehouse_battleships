class InputError(Exception):
    pass


class ShipPlacementError:
    # print out error message

    def __init__(self):
        print("Ship Placement Error")

    def __str__(self):
        return "Ship Placement Error"

    def printerr(self):
        print("Ship Placement Error")

