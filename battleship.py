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
        count = 0
        for ship, val in self.SHIP_INFO:
            print("[ {} ] {}: {} spaces".format(count, ship, val))
            count += 1

    def remove_ship_choice(self, ship):
        try:
            return self.SHIP_INFO.pop(ship)
        except ValueError:
            return False

    def check_sunk(self):
        pass

    def get_location(self):
        pass

    def valid_placement(self, coord, board):
        # TODO - validate ship placement
        coord = coord.split()
        if self.direction == 'VERTICAL_SHIP':
            for point in range(0, self.length):
                print()
                y = int(coord[0]) - (1 + point)
                x = ord(coord[1]) - (97 + point)
                board[y][x] = board.VERTICAL_SHIP

            return True
        elif self.direction == 'HORIZONTAL_SHIP':
            for point in range(0, self.length):
                y = int(coord[0]) - (1 + point)
                x = ord(coord[1]) - (97 + point)

            return True
        else:
            return False


class Aircraft_Carrier(Battleship):
    type = "Aircraft Carrier"
    length = 5
    coord = None
    direction = None


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
