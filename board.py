from player import Player
from battleship import *
import os


class Board:
    BOARD_SIZE = 10

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    # clears the screen based on the esc key being printed
    def clear_screen(self):
        if os.name == 'nt':
            print("\x1b", end=" ")
        else:
            print("\033c", end=" ")

    # Will be called in print_board method
    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'),
                                                      ord('A') +
                                                      self.BOARD_SIZE)]))

    def print_board(self):
        print("\n")
        self.print_board_heading()

        board = []
        row_num = 1

        # prints a nested list with board[x] being the row and board[] being
        # the columns.
        for row in range(self.BOARD_SIZE):
            board.append([self.EMPTY for col in range(self.BOARD_SIZE)])

        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

        print("\n")

    def validate_ship_placement(self):
        # TODO - validate ship placement
        pass