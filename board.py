from helpers import convert_coord

class Board:
    BOARD_SIZE = 10
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    game_board = []

    def place_ship(self, battleship):
        x, y = convert_coord(battleship.coord)

        if battleship.direction == 'VERTICAL_SHIP':
            if x <= self.BOARD_SIZE - battleship.length:
                for point in range(0, battleship.length):
                    self.game_board[x][y] = self.VERTICAL_SHIP
                    x += 1
        else:
            if y <= self.BOARD_SIZE - battleship.length:
                for point in range(0, battleship.length):
                    self.game_board[x][y] = self.HORIZONTAL_SHIP
                    y += 1
        # return new self.game_board
        return self.game_board

    # Will be called in print_board method
    def print_board_heading(self):
        print("   " + " ".join(self.cols))

    def print_board(self, board):
        print("\n")
        self.print_board_heading()

        row_num = 1
        # board = []
        # board = [["A1", "A2", "A3", "A4"],
        #          ["B1", "B2", "B3", "B4"],
        #          ["C1", "C2", "C3", "C4"]]

        # prints a nested list with board[x] being the row and board[] being
        # the columns.
        # for row in range(self.BOARD_SIZE):
        #     board.append([self.EMPTY for col in range(self.BOARD_SIZE)])
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

        print("\n")

    def __init__(self):
        self.cols = [chr(c) for c in range(ord('A'), ord('A') +
                                           self.BOARD_SIZE)]
        self.rows = [num for num in range(1, self.BOARD_SIZE + 1)]
        # self.game_board = [[[ltr, num] for ltr in self.cols[itm] for num in
        #                     self.rows] for itm in range(self.BOARD_SIZE)]

        # Creates a list of a list with EMPTY markers
        # To add marker going horizontal, change in place at game_board[y][x]
        # index x i.e. alphabet = x == x = "-" >> game_board[y]["-"]
        # To add marker going vertical, change in place at game_board[y][x]
        # index y i.e. num = y == y = "|" >> game_board["|"][x]
        self.game_board = [[self.EMPTY for col in self.rows] for row in
                           self.cols]
