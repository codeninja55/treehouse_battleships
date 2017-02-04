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

    type = None
    length = 0
    coord = None
    direction = None

    def __init__(self):
        pass

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
            return False

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
    type = "Aircraft Carrier"
    length = 5
    coord = None
    direction = None
    hit = []
    sunk = False


class Frigate(Battleship):
    type = "Frigate"
    length = 4
    coord = None
    direction = None
    hit = []
    sunk = False


class Submarine(Battleship):
    type = "Submarine"
    length = 3
    coord = None
    direction = None
    hit = []
    sunk = False


class Cruiser(Battleship):
    type = "Cruise"
    length = 3
    coord = None
    direction = None
    hit = []
    sunk = False


class Patrol_Boat(Battleship):
    type = "Patrol Boat"
    length = 2
    coord = None
    direction = None
    hit = []
    sunk = False
