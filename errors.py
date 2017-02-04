class Errors:
    pass


class InputError(Errors):
    pass


class ShipPlacementError(Errors):
    # print out error message
    def __str__(self):
        return "Ship Placement Error"

    def printerr(self):
        print("Ship Placement Error")

