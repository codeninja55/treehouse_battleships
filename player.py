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

        # Print an empty board so the player can decide their placements
        self.player_board.print_board(self.player_board.game_board)

        while len(self.battleship.SHIP_INFO) >= 1:
            # print the list of available battleships to place
            self.battleship.print_ships()

            selectn = (int(input("Choose the index of the ship you would like "
                                "to place? > "))) - 1
            coord = input("Where to place the ship (e.g. a1)? > ").lower()
            # TODO - need to validate input
            directn = input("\nHorizontal [ h ] or Vertical [ v ]? > ").lower()

            # The condition will test if the ship can be placed on the board
            # if its inside the bounds of the board or if there are no other
            # ships already placed on the board. If the condition is not met,
            #  an error will be printed.
            if self.battleship.valid_placement(selectn, coord,
                                               directn, self.player_board):

                # If the ship placement is valid, create an object of
                # subclasses of battleships and make changes to their attributes
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

                # Append a fleet of objects to the ship
                self.fleet.append(ship_choice)

                # Run method from Board class to update player_board
                self.player_board.place_ship(ship_choice)

                # Displays the board with updated ships placed
                self.player_board.print_board(self.player_board.game_board)


    def __str__(self):
        pass

    def __init__(self):
        self.name = input("NAME > ").lstrip().rstrip().lower()
        self.confirmation = input("Are you ready to place your battleships? "
                             "Y/n > ").lower()
