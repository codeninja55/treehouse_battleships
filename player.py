from battleship import *
from board import Board
from errors import ShipPlacementError

class Player():
    fleet = []
    hit = []
    missed = []
    # Create new instance of Battleship() and Board() to implement methods
    battleship = Battleship()
    player_board = Board()

    def ship_placement(self):
        if self.confirmation == 'n':
            input("When ready, press enter/return to continue > ")
            self.ship_placement()

        self.player_board.print_board(self.player_board.game_board)

        while len(self.battleship.SHIP_INFO) >= 1:
            # print the list of available battleships to place
            self.battleship.print_ships()

            selectn = (int(input("Choose the index of the ship you would like "
                                "to place? > "))) - 1
            coord = input("Where to place the ship (e.g. a1)? > ").lower()
            # TODO - need to validate input
            directn = input("\nHorizontal [ h ] or Vertical [ v ]? > ").lower()

            # TODO - need to validate ship placement
            if self.battleship.valid_placement(selectn, coord,
                                               directn, self.player_board):
                print("Success, ship placed on board.")
                # Method to pop from list of ships and create battleship obj.
                # Each battleship object will have attributes changed based on
                # player input such as coordinates and directions of ship.
                ship_choice = self.battleship.remove_ship_choice(selectn)[0]
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

                if directn == "v":
                    ship_choice.direction = "VERTICAL_SHIP"
                else:
                    ship_choice.direction = "HORIZONTAL_SHIP"

                self.fleet.append(ship_choice)
                # TODO - need to display board with ship placements
                self.player_board.print_board(self.player_board.game_board)


    def __str__(self):
        pass

    def __init__(self):
        self.name = input("NAME > ").lstrip().rstrip().lower()
        self.confirmation = input("Are you ready to place your battleships? "
                             "Y/n > ").lower()
