from helpers import *
from player import Player


class Game:
    def game_progress(self, player, opponent):
        # check if each player still has a ship on the board
        # check each player's fleet for sunk value == false ????

        if len(opponent.fleet) == 0:
            print("#" * 60)
            print("\n")
            print("{}'s fleet has been sunk.".format(opponent.name))
            print("\n{} HAS WON THE GAME!!!".format(player.name.upper()))
            print("\n")
            print("#" * 60)
            return False
        else:
            for ship in opponent.fleet:
                if ship.sunk:
                    try:
                        opponent.fleet.remove(ship)
                        print(opponent.fleet)
                    except (IndexError, ValueError):
                        continue

            return True

    def update_board(self, opponent, guess):
        # Update the board after every guess
        # Take guess value and change the board of the opponents guess board.
        board = opponent.player_board
        guess_board = opponent.guess_board
        x, y = guess

        for ship in opponent.fleet:
            if ship.sunk:
                for coord in ship.positions:
                    x, y = coord
                    guess_board.game_board[x][y] = guess_board.SUNK
                    board.game_board[x][y] = board.SUNK
                print("\nYou have sunk a {}.".format(ship.type))
            else:
                continue

        if board.game_board[x][y] != board.SUNK:
            if board.game_board[x][y] == board.EMPTY:
                guess_board.game_board[x][y] = board.MISS
                print("\nOh you have missed!")
            elif board.game_board[x][y] == board.VERTICAL_SHIP or \
                    board.game_board[x][y] == board.HORIZONTAL_SHIP:
                guess_board.game_board[x][y] = board.HIT
                print("\nThat was a HIT!")

    def update_battleships(self, opponent, guess):
        for ship in opponent.fleet:
            for coord in ship.positions:
                if coord == guess:
                    ship.hit.append(guess)

            if set(ship.positions) == set(ship.hit):
                ship.sunk = True

    def player_guess(self, player, opponent):
        # take the player's guess and add it to the guess_board of the opp
        # return the player obj and the guess
        self.print_guess_boards(player, opponent)
        self.print_guess_boards(opponent, player)

        guess = input("\n{}, guess a location to hit > ".format(
            player.name)).lower()

        guess_valid = validate_coord(player.player_board, guess)

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
        print("\n{}'S GUESS BOARD".format(player.name.upper()))
        opponent.player_board.print_board(opponent.guess_board.game_board)

    def player_turn(self, player, opponent):
        if self.game_progress(player, opponent):
            clear()
            print("\n{}, it is your turn now.".format(player.name))
            self.player_guess(player, opponent)
            print("\n{} your turn is finished.".format(player.name))
            proceed_confirm()

    # def play(self, player1, player2):
    #     """This method..."""
    #
    #     while self.game_progress(player1, player2):
    #         self.player_turn(player1, player2)
    #         self.player_turn(player2, player1)

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
        clear()
        player1, player2 = self.setup_game()
        # self.play(player1, player2)
        self.player_turn(player1, player2)
        self.player_turn(player2, player1)

if __name__ == '__main__':
    Game()
