from battleship import *
from board import Board
from errors import ShipPlacementError

class Player():
    fleet = []
    hit = []
    missed = []

    def ship_placement(self):
        # TODO - prompt user to place a ship

        self.confirmation = input("Are you ready to place your battleships? "
                                  "Y/n > ").lower()

        if self.confirmation == 'n':
            input("When ready, press enter/return to continue > ")
            self.ship_placement()

        # create new instance of Battleship() to implement methods
        battleship = Battleship()
        player_board = Board()

        while len(battleship.SHIP_INFO) >= 1:
            # print the list of available battleships to place
            battleship.print_ships()

            selectn = int(input("Choose the index of the ship you would like "
                                "to place > "))
            coord = input("Place the ship (e.g. a1) > ").lower()
            # TODO - need to validate input
            # TODO - need to validate ship placement
            # TODO - need to display board with ship placements
            direction = input("Horizontal [ h ] or Vertical [ v ] > ").lower()

            # Method to pop from list of ships and create battleship objects.
            # Each battleship object will have attributes changed based on
            # player input such as coordinates and directions of ship.
            ship_choice = battleship.remove_ship_choice(selectn)[0]
            if ship_choice == "Aircraft Carrier":
                ship_choice = Aircraft_Carrier()
            elif ship_choice == "Frigate":
                ship_choice = Frigate()
            elif ship_choice == "Submarine":
                ship_choice = Submarine()
            elif ship_choice == "Cruiser":
                ship_choice = Cruiser()
            elif ship_choice == "Patrol Boat":
                ship_choice = Patrol_Boat()
            else:
                break

            ship_choice.coord = coord
            if direction == "v":
                ship_choice.direction = "VERTICAL_SHIP"
            else:
                ship_choice.direction = "HORIZONTAL_SHIP"

            if ship_choice.valid_placement(ship_choice.coord, player_board):
                self.fleet.append(ship_choice)
            else:
                print(ShipPlacementError())


    def __str__(self):
        pass

    def __init__(self):
        self.name = input("NAME > ").lstrip().rstrip().lower()
