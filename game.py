from helpers import *
from player import Player
from sys import exit


class Game:
    def print_winner(self, player, opponent):
        print("\n\n" + "#" * 60 + "\n")
        print("{}'s fleet has been sunk.".format(opponent.name))
        print("\n{} HAS WON THE GAME!!!".format(player.name.upper()))
        print("\n" + "#" * 60 + "\n")
        exit()

    def update_board(self, opponent, guess):
        """This method will update the guess board from the opposing player
        as each player makes a guess."""

        board = opponent.player_board
        guess_board = opponent.guess_board
        x, y = guess

        # Check each ship in the opponent's fleet and if they sunk value has
        # been changed to True, then update the board with the SUNK value
        for ship in opponent.fleet:
            if ship.sunk:
                for coord in ship.positions:
                    x, y = coord
                    guess_board.game_board[x][y] = guess_board.SUNK
                    board.game_board[x][y] = board.SUNK

                print("\nYou have sunk {}'s {}.".format(
                    opponent.name.capitalize(), ship.type))
            else:
                continue

        # If the ship has not already been sunk, check if it's a hit or miss
        # based on the player's board completed at setup.
        if board.game_board[x][y] != board.SUNK:
            if board.game_board[x][y] == board.EMPTY:
                guess_board.game_board[x][y] = board.MISS
                print("\nOh you have missed!")
            elif board.game_board[x][y] == board.VERTICAL_SHIP or \
                    board.game_board[x][y] == board.HORIZONTAL_SHIP:
                guess_board.game_board[x][y] = board.HIT
                print("\nThat was a HIT!")

    def update_battleships(self, opponent, guess):
        """This method will update each battleship by comparing a set
        positions for the battleship and a list of guesses by the player. If
        those sets match, it will update the sunk attribute to True"""

        for ship in opponent.fleet:
            for coord in ship.positions:
                if coord == guess:
                    ship.hit.append(guess)

            if set(ship.positions) == set(ship.hit):
                ship.sunk = True

    def update_fleet(self, opponent):
        """This method will go through the opposing player's fleet and check
        if the sunk attribute has been set to True. If so, it will attempt to
        remove it from the fleet"""

        for ship in opponent.fleet:
            if ship.sunk:
                try:
                    opponent.fleet.remove(ship)
                    print(opponent.fleet)
                except (IndexError, ValueError):
                    continue

    def player_guess(self, player, opponent):
        """This method will take the player's guess and check if it is
        firstly valid. If valid, it will call the methods update_battleships,
        update_board, and print_guess_boards."""

        self.print_guess_boards(player, opponent)
        self.print_guess_boards(opponent, player)

        guess = input("\n{}, guess a location to hit > ".format(
            player.name)).lower()

        guess_valid = player.player_board.validate_coord(guess)

        # Check's the guess if it was a hit or miss

        if not guess_valid:
            self.player_guess(player, opponent)
        else:
            clear()
            guess_coord = convert_coord(guess_valid)
            print(
                "\n{}, you have guessed: {}".format(player.name, guess.upper()))
            player.guesses.append(guess_coord)
            self.update_battleships(opponent, guess_coord)
            self.update_board(opponent, guess_coord)
            self.print_guess_boards(player, opponent)

    def print_guess_boards(self, player, opponent):
        """This method will print the guess board as part of the opposing
        player's Player object."""

        print("\n{}'S GUESS BOARD".format(player.name.upper()))
        opponent.player_board.print_board(opponent.guess_board.game_board)

    def player_turn(self, player, opponent):
        """This method will first update the player's fleet and check if they
        any remaining battleships. If not, it will declare the opposing
        player as the winner. Otherwise, it will allow the player to make an
        input as a guess and begin the process of checking if that guess was
        a hit or miss."""

        clear()

        self.update_fleet(player)

        if not player.fleet:
            self.print_winner(opponent, player)
        else:
            print("\n{}, it is your turn now.".format(player.name))
            self.player_guess(player, opponent)
            print("\n{} your turn is finished.".format(player.name))
            proceed_confirm()

    def setup_game(self):
        """This method will ask the players for their names and begin to
        place their ships on the board. It returns a tuple of player objects."""
        # Instantiate two players, ask for name, then place ships
        name1 = input("\nPLAYER 1 NAME > ").lstrip().rstrip().lower()
        name2 = input("\nPLAYER 2 NAME > ").lstrip().rstrip().lower()
        clear()
        print("\nPlayer 1: {}\n\nPlayer 2: {}".format(name1.capitalize(),
                                                        name2.capitalize()))
        proceed_confirm()

        clear()
        player1 = Player(name1, 1)
        confirmation = input("\n{}, are you ready to place your battleships? "
                             "[Y] / [n] > ".format(name1.capitalize())).lower()

        if confirmation != 'n':
            clear()
            player1.ship_placement()
        else:
            proceed_confirm()

        print("\n{} (Player: {}), you have now completed your setup of "
              "Battleship.".format(name1.capitalize(), player1.player_num))
        print("\nPlease pass the game to {}.".format(name2.capitalize()))

        proceed_confirm()
        clear()

        player2 = Player(name2, 2)

        confirmation = input("\n{}, are you ready to place your battleships? "
                             "[Y] / [n] > ".format(name2.capitalize())).lower()

        if confirmation != 'n':
            clear()
            player2.ship_placement()
        else:
            proceed_confirm()

        print("\n{} (Player: {}), you have now completed your setup of "
              "Battleship.".format(name2.capitalize(), player2.player_num))

        print("\nThe game will begin now...")
        proceed_confirm()

        return player1, player2

    def __init__(self):
        """This class will begin the setup process and the gamplay for
        Battleships."""

        clear()
        player1, player2 = self.setup_game()
        # self.play(player1, player2)
        while player1.fleet and player2.fleet:
            self.player_turn(player1, player2)
            self.player_turn(player2, player1)


if __name__ == '__main__':
    Game()
