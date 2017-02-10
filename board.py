from helpers import convert_coord
from errors import InputError

class Board:
    BOARD_SIZE = 10
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    def validate_coord(self, coord):
        coord = coord.lstrip().rstrip().lower().replace(' ', '')

        if len(coord) <= 1:
            InputError('coordinates', coord)
            return False
        else:
            if coord[0].isnumeric() and not coord[1].isnumeric():
                try:
                    if int(coord[0]) not in self.rows:
                        InputError('board_boundaries', coord)
                        return False
                except ValueError:
                    InputError('coordinate_int', coord)
                    return False
                else:
                    if coord[1:].upper() not in self.cols:
                        InputError('board_boundaries', coord)
                        return False
                    else:
                        coord = str(coord[1]) + str(coord[0])
                        return self.validate_coord(coord)
            elif coord[0:2].isnumeric():
                try:
                    if int(coord[0:2]) not in self.rows:
                        InputError('board_boundaries', coord)
                        return False
                except ValueError:
                    InputError('coordinate_int', coord)
                    return False
                else:
                    if coord[2:].upper() not in self.cols:
                        InputError('board_boundaries', coord)
                        return False
                    else:
                        coord = str(coord[2]) + str(coord[0:2])
                        return self.validate_coord(coord)
            else:
                try:
                    if int(coord[1]) not in self.rows:
                        InputError('board_boundaries', coord)
                        return False
                except ValueError:
                    InputError('coordinate_int', coord)
                    return False
                else:
                    if coord[0].upper() not in self.cols:
                        InputError('board_boundaries', coord)
                        return False
                    else:
                        return coord

    def place_ship(self, battleship):
        """Gets coordinates from player class and a convert coordinates
        helper function.Uses the battleship object passed in and the
        index returned as x and y values to change in place the values found
        in the nested list of game_board. Once complete, returns the
        game_board"""
        x, y = convert_coord(battleship.coord)

        if battleship.orientation == 'v':
            if x <= self.BOARD_SIZE - battleship.length:
                for point in range(0, battleship.length):
                    # Place a tuple of coordinates into the positions list
                    battleship.positions.append((x, y))
                    self.game_board[x][y] = self.VERTICAL_SHIP
                    x += 1
        else:
            if y <= self.BOARD_SIZE - battleship.length:
                for point in range(0, battleship.length):
                    battleship.positions.append((x, y))
                    self.game_board[x][y] = self.HORIZONTAL_SHIP
                    y += 1

        return self.game_board

    # Will be called in print_board method
    def print_board_heading(self):
        """Prints a row of alphabet letters found in a list based on size of
        the board size."""
        print("   " + " ".join(self.cols))

    def print_board(self, board):
        """Prints the board based on the board argument being a nested list."""
        print("\n")
        self.print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
        print("\n")

    def __init__(self):
        self.cols = [chr(c) for c in range(ord('A'), ord('A') +
                                           self.BOARD_SIZE)]
        self.rows = [num for num in range(1, self.BOARD_SIZE + 1)]
        self.game_board = [[self.EMPTY for col in self.rows] for row in
                           self.cols]
