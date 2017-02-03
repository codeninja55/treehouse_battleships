from board import Board
from battleship import *

class Player:
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

        battleship = Battleship()

        while len(battleship.SHIP_INFO) >= 1:
            battleship.print_ships()

            selectn = int(input("Choose the index of the ship you would like "
                                "to place > "))
            coord = input("Place the ship (e.g. a1) > ").lower()
            direction = input("Horizontal [ h ] or Vertical [ v ] > ").lower()

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

            self.fleet.append(ship_choice)

    def __str__(self):
        pass

    def __init__(self, **kwargs):
        # TODO - prompt the player for their names
        self.name = input("NAME > ").lstrip().rstrip().lower()

        # self.name = input()

        for key, value in kwargs.items():
            setattr(self, key, value)
