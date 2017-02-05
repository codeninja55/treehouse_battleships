from errors import ShipPlacementError, CoordinatesOccupiedError
from helpers import convert_coord


class Battleship:
    # provided by Treehouse's original project file
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Frigate", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)]

    def __init__(self):
        self.type = None
        self.length = 0
        self.coord = None
        self.direction = None
        self.positions = []
        self.hit = []
        self.sunk = False

    def print_ships(self):
        """This method iterates through the SHIP_INFO list and prints each
        one so that players can select the battleship based on index"""
        count = 1
        print("\n")
        for ship, val in self.SHIP_INFO:
            print("[ {} ] {}: {} spaces".format(count, ship, val))
            count += 1
        print("\n")

    def remove_ship_choice(self, ship):
        """This method removes and returns a tuple from the list in SHIP_INFO"""
        try:
            return self.SHIP_INFO.pop(ship)
        except ValueError:
            return None

    def valid_placement(self, selectn, coord, directn, board):
        """This method will take arguments of selection index, coordinates,
        and direction, as well as the player's board. It will check those
        arguments to validate the placement of ship on the board. If
        validation is successful, the method will return true which is used
        to check for validation."""
        # Unpacks tuples from convert_coord function that converts the
        # coordinates to an index value.
        x, y = convert_coord(coord)

        if directn == 'v':
            # Checks if the battleship fits within the boundary of the board
            if x <= board.BOARD_SIZE - self.SHIP_INFO[selectn][1]:
                for point in range(0, self.SHIP_INFO[selectn][1]):
                    # Checks if points on the board are EMPTY
                    if board.game_board[x][y] != board.EMPTY:
                        CoordinatesOccupiedError()
                        return False
                    x += 1
            else:
                ShipPlacementError()
                return False
        elif directn == 'h':
            if y <= board.BOARD_SIZE - self.SHIP_INFO[selectn][1]:
                for point in range(0, self.SHIP_INFO[selectn][1]):
                    if board.game_board[x][y] != board.EMPTY:
                        CoordinatesOccupiedError()
                        return False
                    y += 1
            else:
                ShipPlacementError()
                return False
        else:
            return False

        return True


class Aircraft_Carrier(Battleship):
    def __init__(self, coord, direction):
        Battleship.__init__(self)
        self.type = "Aircraft Carrier"
        self.length = 5
        self.coord = coord
        self.direction = direction


class Frigate(Battleship):
    def __init__(self, coord, direction):
        Battleship.__init__(self)
        self.type = "Frigate"
        self.length = 4
        self.coord = coord
        self.direction = direction


class Submarine(Battleship):
    def __init__(self, coord, direction):
        Battleship.__init__(self)
        self.type = "Submarine"
        self.length = 3
        self.coord = coord
        self.direction = direction


class Cruiser(Battleship):
    def __init__(self, coord, direction):
        Battleship.__init__(self)
        self.type = "Cruise"
        self.length = 3
        self.coord = coord
        self.direction = direction


class Patrol_Boat(Battleship):
    def __init__(self, coord, direction):
        Battleship.__init__(self)
        self.type = "Patrol Boat"
        self.length = 2
        self.coord = coord
        self.direction = direction
