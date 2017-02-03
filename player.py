from board import Board

class Player:
    def validate_ship(self):
        # TODO - validate ship placement
        pass

    def ship_placement(self):
        # TODO - prompt user to place a ship
        # For each ship, ask if they want the ship to be oriented horizontally
        # or vertically then ask which location on the board the first ships
        # should be placed at
        # E.g. Place the location of the aircraft carrier (5 spaces): a2
        # E.g. Is it horizontal? (Y)/N: n
        # TODO - prompt second player to place their ships
        pass

    def __str__(self):
        pass

    def __init__(self, **kwargs):
        # TODO - prompt the player for their names
        # self.name = input()

        for key, value in kwargs.items():
            setattr(self, key, value)
