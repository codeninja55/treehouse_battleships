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
