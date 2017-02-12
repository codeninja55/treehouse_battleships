from errors import ShipPlacementError
from helpers import convert_coord


class Battleship:
    def valid_placement(self, selectn, coord, orientation, board):
        """This method will take arguments of selection index, coordinates,
        and orientation, as well as the player's board. It will check those
        arguments to validate the placement of ship on the board. If
        validation is successful, the method will return true which is used
        to check for validation."""
        # Unpacks tuples from convert_coord function that converts the
        # coordinates to an index value.
        x, y = convert_coord(coord)

        if orientation == 'v':
            # Checks if the battleship fits within the boundary of the board
            if x <= board.BOARD_SIZE - self.ship_info[selectn][1]:
                for point in range(0, self.ship_info[selectn][1]):
                    # Checks if points on the board are EMPTY
                    if board.game_board[x][y] != board.EMPTY:
                        return False
                    x += 1
                return True
            else:
                ShipPlacementError('outofbounds', coord, directn)
                return False
        elif orientation == 'h':
            if y <= board.BOARD_SIZE - self.ship_info[selectn][1]:
                for point in range(0, self.ship_info[selectn][1]):
                    if board.game_board[x][y] != board.EMPTY:
                        return False
                    y += 1
                return True
            else:
                ShipPlacementError('outofbounds', coord, orientation)
                return False
        else:
            return False

    def print_ships(self):
        """This method iterates through the ship_info list and prints each
        one so that players can select the battleship based on index"""
        count = 1
        for ship, val in self.ship_info:
            print("[ {} ] {}: {} spaces".format(count, ship, val))
            count += 1
        print("\n")

    def get_next_ship(self, ship):
        """This method removes and returns a tuple from the list in
        ship_info. If there are no more battleships to place, will return a 0
        so the ship_placement() method can break the while loop"""
        try:
            return self.ship_info.pop(ship)
        except (IndexError, ValueError):
            return False

    def __init__(self):
        # provided by Treehouse's original project file
        self.ship_info = [
            ("Aircraft Carrier", 5),
            ("Frigate", 4),
            ("Submarine", 3),
            ("Cruiser", 3),
            ("Patrol Boat", 2)]

        self.type = None
        self.length = 0
        self.coord = None
        self.orientation = None
        self.positions = []
        self.hit = []
        self.sunk = False

class Aircraft_Carrier(Battleship):
    def __init__(self, coord, orientation):
        Battleship.__init__(self)
        self.type = "Aircraft Carrier"
        self.length = 5
        self.coord = coord
        self.orientation = orientation


class Frigate(Battleship):
    def __init__(self, coord, orientation):
        Battleship.__init__(self)
        self.type = "Frigate"
        self.length = 4
        self.coord = coord
        self.orientation = orientation


class Submarine(Battleship):
    def __init__(self, coord, orientation):
        Battleship.__init__(self)
        self.type = "Submarine"
        self.length = 3
        self.coord = coord
        self.orientation = orientation


class Cruiser(Battleship):
    def __init__(self, coord, orientation):
        Battleship.__init__(self)
        self.type = "Cruise"
        self.length = 3
        self.coord = coord
        self.orientation = orientation


class Patrol_Boat(Battleship):
    def __init__(self, coord, orientation):
        Battleship.__init__(self)
        self.type = "Patrol Boat"
        self.length = 2
        self.coord = coord
        self.orientation = orientation
