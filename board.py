import os
import random


class Board:
    BOARD_SIZE = 5

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    def clear_screen(self):
        if os.name == 'nt':
            print("\x1b", end="")
        else:
            print("\033c", end="")

    # Will be called in print_board method
    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'),
                                                      ord('A') +
                                                      self.BOARD_SIZE)]))

    # TODO - display boards to the screen
    def print_board(self):
        self.print_board_heading()

        board = []
        row_num = 1

        for row in range(self.BOARD_SIZE):
            board.append([self.EMPTY for col in range(self.BOARD_SIZE)])

        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1


class Battleships(Board):
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)]

    def get_random(self):
        # get a random battleship from SHIP_INFO
        # allow user to place ship on board
        pass