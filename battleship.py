from errors import ShipPlacementError


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
        count = 1
        print("\n")
        for ship, val in self.SHIP_INFO:
            print("[ {} ] {}: {} spaces".format(count, ship, val))
            count += 1
        print("\n")

    def remove_ship_choice(self, ship):
        try:
            return self.SHIP_INFO.pop(ship)
        except ValueError:
            return False

    def check_sunk(self):
        pass

    def get_location(self):
        pass

    # Will take coord, ship selection, and direction from player's battleship
    # choice and the player's board to check if it's possible to place a
    # battle in that place.
    def valid_placement(self, selectn, coord, directn, board):
        # TODO - validate ship placement
        y = ord(coord[0]) - 97

        if len(coord) > 2:
            x = int(coord[1:]) - 1
        else:
            x = int(coord[1]) - 1

        if directn == 'v':
            if x <= board.BOARD_SIZE - self.SHIP_INFO[selectn][1]:
                for point in range(0, self.SHIP_INFO[selectn][1]):
                    # print("x: {} | y: {} | point: {}".format(str(x),
                    #                                          str(y),
                    #                                          str(point)))
                    board.game_board[x][y] = board.VERTICAL_SHIP
                    x += 1
            else:
                ShipPlacementError()
                return False
        elif directn == 'h':
            if y <= board.BOARD_SIZE - self.SHIP_INFO[selectn][1]:
                for point in range(0, self.SHIP_INFO[selectn][1]):
                    # print("x: {} | y: {} | point: {}".format(str(x),
                    #                                          str(y),
                    #                                          str(point)))
                    board.game_board[x][y] = board.HORIZONTAL_SHIP
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


class Submarine(Battleship):
    type = "Submarine"
    length = 3
    coord = None
    direction = None


class Cruiser(Battleship):
    type = "Cruise"
    length = 3
    coord = None
    direction = None


class Patrol_Boat(Battleship):
    type = "Patrol Boat"
    length = 2
    coord = None
    direction = None
