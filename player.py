from battleship import *
from board import Board
from errors import InputError
from helpers import clear


class Player():
    def validate_input(self, user_input):
        if isinstance(user_input, int):
            if user_input in list(range(0, len(self.battleship.SHIP_INFO))):
                return True
            else:
                InputError().index_selection()
                return False
        elif isinstance(user_input, str):
            user_input = user_input.lstrip().rstrip().lower()

            if user_input == 'n':
                while True:
                    inp = input("When ready, press enter/return to continue > ")
                    if inp == "":
                        return True
            elif user_input == 'h':
                return True
            elif user_input == 'v':
                return True
            elif len(user_input) > 1 and user_input[0].upper() in \
                    self.player_board.cols:
                if user_input[1:].isnumeric():
                    if int(user_input[1:]) in self.player_board.rows:
                        return True
                    else:
                        InputError().coordinates()
                        return False
                else:
                    InputError().coordinates()
                    return False
        else:
            return False

        return True

    def ship_placement(self):
        clear()
        # Print an empty board so the player can decide their placements
        self.player_board.print_board(self.player_board.game_board)

        while len(self.battleship.SHIP_INFO) != 0:
            # print the list of available battleships to place
            self.battleship.print_ships()

            selectn = input("Choose the index of the ship you would like "
                            "to place? > ")
            try:
                selectn = int(selectn) - 1
            except ValueError:
                InputError().value()
                self.ship_placement()

            if not self.validate_input(selectn):
                self.ship_placement()

            coord = input("Where to place the ship (e.g. a1)? > ").lower()

            if not self.validate_input(coord):
                self.ship_placement()

            directn = input("Horizontal [ h ] or Vertical [ v ]? > ").lower()

            if not self.validate_input(directn):
                self.ship_placement()

            # The condition will test if the ship can be placed on the board
            # if its inside the bounds of the board or if there are no other
            # ships already placed on the board. If the condition is not met,
            #  an error will be printed.
            if self.battleship.valid_placement(selectn, coord,
                                               directn, self.player_board):

                # If the ship placement is valid, create an object of
                # subclasses of battleships and make changes to their attributes
                ship_choice = self.battleship.remove_ship_choice(selectn)[0]

                if directn == "v":
                    direction = "VERTICAL_SHIP"
                else:
                    direction = "HORIZONTAL_SHIP"

                if ship_choice == "Aircraft Carrier":
                    ship_choice = Aircraft_Carrier(coord, direction)
                elif ship_choice == "Frigate":
                    ship_choice = Frigate(coord, direction)
                elif ship_choice == "Submarine":
                    ship_choice = Submarine(coord, direction)
                elif ship_choice == "Cruiser":
                    ship_choice = Cruiser(coord, direction)
                elif ship_choice == "Patrol Boat":
                    ship_choice = Patrol_Boat(coord, direction)
                else:
                    break

                # Append a fleet of objects to the ship
                self.fleet.append(ship_choice)

                # Run method from Board class to update player_board
                self.player_board.place_ship(ship_choice)

                # Displays the board with updated ships placed
                clear()
                self.player_board.print_board(self.player_board.game_board)

                if len(self.battleship.SHIP_INFO ) == 0:
                    clear()
                    print("\n{} (Player: {}), you have now completed your "
                          "setup of Battleship.".
                          format(self.name.capitalize(), self.player_num))

    def __str__(self):
        return """Player: {}
        Name: {}
        Board: {}
        """.format(self.player_num, self.name, self.player_board.print_board(
            self.player_board.game_board))

    def __init__(self, name, player_num):
        self.fleet = []
        self.hit = []
        self.missed = []
        self.player_num = player_num
        # Create new instance of Battleship and Board objects to implement
        # methods
        self.battleship = Battleship()
        self.player_board = Board()

        self.name = name
        self.confirmation = input("\nAre you ready to place your battleships? "
                             "[ Y ] / [ n ] > ").lower()
        # if not self.validate_input(self.confirmation):
        #     InputError().confirmation_error()

