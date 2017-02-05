from helpers import convert_coord


class Board:
    BOARD_SIZE = 10
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    def place_ship(self, battleship):
        """Gets coordinates from player class and a convert coordinates
        helper function.Uses the battleship object passed in and the
        index returned as x and y values to change in place the values found
        in the nested list of game_board. Once complete, returns the
        game_board"""
        x, y = convert_coord(battleship.coord)

        if battleship.direction == 'VERTICAL_SHIP':
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

    def __init__(self):
        self.cols = [chr(c) for c in range(ord('A'), ord('A') +
                                           self.BOARD_SIZE)]
        self.rows = [num for num in range(1, self.BOARD_SIZE + 1)]
        self.game_board = [[self.EMPTY for col in self.rows] for row in
                           self.cols]
