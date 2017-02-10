from battleship import *
from board import Board
from errors import InputError
from helpers import clear


class Player:
    def ship_placement(self):
        while len(self.battleship.ship_info) != 0:

            selection = self.get_selection()
            coord = self.get_coordinates()
            orientation = self.get_orientation()

            # The condition will test if the ship can be placed on the board
            # if its inside the bounds of the board or if there are no other
            # ships already placed on the board. If the condition is not met,
            #  an error will be printed.
            if self.battleship.valid_placement(selection, coord,
                                               orientation, self.player_board):

                # If the ship placement is valid, create an object of
                # subclasses of battleships and make changes to their attributes
                ship_choice = self.battleship.get_next_ship(selection)[0]

                if ship_choice == "Aircraft Carrier":
                    ship_choice = Aircraft_Carrier(coord, orientation)
                elif ship_choice == "Frigate":
                    ship_choice = Frigate(coord, orientation)
                elif ship_choice == "Submarine":
                    ship_choice = Submarine(coord, orientation)
                elif ship_choice == "Cruiser":
                    ship_choice = Cruiser(coord, orientation)
                elif ship_choice == "Patrol Boat":
                    ship_choice = Patrol_Boat(coord, orientation)
                else:
                    break

                # Append a fleet of objects to the ship
                self.fleet.append(ship_choice)

                # Run method from Board class to update player_board
                self.player_board.place_ship(ship_choice)

                # Displays the board with updated ships placed
                clear()
            else:
                ShipPlacementError('occupied', coord, orientation)
                self.ship_placement()

    def get_orientation(self):
        orientation = input("Horizontal [h] or Vertical [v]? > ").lower()

        if orientation != 'v' and orientation != 'h':
            InputError('orientation', orientation)
            self.player_board.print_board(self.player_board.game_board)
            return self.get_orientation()
        else:
            return orientation

    def get_coordinates(self):
        coord = input("Coordinates to place the ship (e.g. a1)? > ").lower()

        coord_valid = self.player_board.validate_coord(coord)
        if not coord_valid:
            self.player_board.print_board(self.player_board.game_board)
            return self.get_coordinates()
        else:
            return coord_valid

    def get_selection(self):
        self.player_board.print_board(self.player_board.game_board)
        self.battleship.print_ships()

        selection = input("Choose the index (e.g. 1)? > ")

        try:
            selection = int(selection) - 1
        except ValueError:
            InputError('value', selection)
            return self.get_selection()
        else:
            if selection not in list(range(0, len(self.battleship.ship_info))):
                selection = selection + 1
                InputError('index_selection', selection)
                return self.get_selection()
            else:
                return selection

    def __str__(self):
        self.player_board.print_board(self.player_board.game_board)
        return """Player: {} \nName: {}""".format(self.player_num, self.name)

    def __init__(self, name, player_num):
        self.fleet = []
        self.guesses = []
        self.name = name.capitalize()
        self.player_num = player_num
        # Create new instance of Battleship and Board objects to implement
        # methods
        self.battleship = Battleship()
        self.player_board = Board()
        self.guess_board = Board()
