from helpers import clear, proceed_confirm, convert_coord
from player import Player
from errors import InputError


class Game:
    def game_progress(self, player, guess):
        # check if each player still has a ship on the board
        # check each player's fleet for sunk value == false ????


        # if a player guess has completely destroyed a ship
            # end game
            # return a false
            # TODO - declare a winner
        # else
            # return true so game can continue
        return False

    def update_board(self, opponent, guess):
        # Update the board after every guess
        # Take guess value and change the board of the opponents guess board.
        board = opponent.player_board
        guess_board = opponent.guess_board
        x, y = guess

        for ship in opponent.fleet:
            if ship.sunk == True:
                for coord in ship.positions:
                    x, y = coord
                    guess_board.game_board[x][y] = guess_board.SUNK
                    board.game_board[x][y] = board.SUNK
            else:
                break

        if board.game_board[x][y] != board.SUNK:
            if board.game_board[x][y] == board.EMPTY:
                guess_board.game_board[x][y] = board.MISS
            elif board.game_board[x][y] == board.VERTICAL_SHIP or \
                board.game_board[x][y] == board.HORIZONTAL_SHIP:

                guess_board.game_board[x][y] = board.HIT

    def update_battleships(self, opponent, guess):
        for ship in opponent.fleet:
            for coord in ship.positions:
                if coord == guess:
                    ship.hit.append(guess)

            if set(ship.positions) == set(ship.hit):
                ship.sunk = True


    def validate_guess(self, player, guess):
        guess = guess.lstrip().rstrip().lower()
        x, y = convert_coord(guess)
        # TODO - validate guess
        if isinstance(guess, str):
            if len(guess) > 1 and \
                    guess[0].upper() in player.player_board.cols and \
                    guess[1:].isnumeric() and \
                    int(guess[1:]) in player.player_board.rows and \
                    (x, y) not in player.guesses:
                return True
            else:
                return False
        else:
            print("Not a string")
            return False


    def player_guess(self, player, opponent):
        # take the player's guess and add it to the guess_board of the opp
        # return the player obj and the guess

        guess = input("\n{}, guess a location to hit > ".format(
            player.name)).lower()

        # TODO - display guess results
        print("\n{}, you have guessed: {}".format(player.name, guess.upper()))

        if self.validate_guess(player, guess):
            g_coord = convert_coord(guess)
            player.guesses.append(g_coord)
            self.update_battleships(opponent, g_coord)
            self.update_board(opponent, g_coord)
        else:
            InputError().guess()
            self.player_guess(player, opponent)

        # return guess

    def play(self, player1, player2):
        # TODO - allow players to take turns
        print("\n{}'S GUESS BOARD".format(player1.name.upper()))
        player1.player_board.print_board(player2.guess_board.game_board)
        print("\n")
        print("\n{}'S GUESS BOARD".format(player2.name.upper()))
        player2.player_board.print_board(player1.guess_board.game_board)
        print("\n")

        # Use this marker for testing purposes until game_progress method done
        game_progress = True

        while game_progress:
            clear()

            print("\n{}'S GUESS BOARD".format(player1.name.upper()))
            player1.player_board.print_board(player2.guess_board.game_board)
            print("\n")
            print("\n{}'S GUESS BOARD".format(player2.name.upper()))
            player2.player_board.print_board(player1.guess_board.game_board)

            print("\n{}, it is your turn now.".format(player1.name))
            self.player_guess(player1, player2)
            print("\n{} your turn is finished.".format(player1.name))

            proceed_confirm()
            clear()

            print("\n{}'S GUESS BOARD".format(player1.name.upper()))
            player1.player_board.print_board(player2.guess_board.game_board)
            print("\n")
            print("\n{}'S GUESS BOARD".format(player2.name.upper()))
            player2.player_board.print_board(player1.guess_board.game_board)

            print("\n{}, it is your turn now.".format(player2.name))
            self.player_guess(player2, player1)
            print("\n{} your turn is finished.".format(player2.name))

        # while self.game_progress(player1, player2):
        #     break

    def setup_game(self):
        """This method will ask the players for their names and begin to
        place their ships on the board. It returns a tuple of player objects."""
        # Instantiate two players, ask for name, then place ships
        name1 = input("\nPLAYER 1 NAME > ").lstrip().rstrip().lower()
        name2 = input("\nPLAYER 2 NAME > ").lstrip().rstrip().lower()

        player1 = Player(name1, 1)
        confirmation = input("\n{}, are you ready to place your battleships? "
                             "[Y] / [n] > ".format(name1.capitalize())).lower()

        if confirmation != 'n':
            player1.ship_placement()
        else:
            proceed_confirm()

        print("\n{} (Player: {}), you have now completed your setup of "
              "Battleship.".format(name1.capitalize(), player1.player_num))
        print("\n\n")

        proceed_confirm()
        clear()

        player2 = Player(name2, 2)

        confirmation = input("\n{}, are you ready to place your battleships? "
                             "[Y] / [n] > ".format(name2.capitalize())).lower()

        if confirmation != 'n':
            player2.ship_placement()
        else:
            proceed_confirm()

        print("\n{} (Player: {}), you have now completed your setup of "
              "Battleship.".format(name2.capitalize(), player2.player_num))

        print("\nThe game will begin now...")
        proceed_confirm()

        return player1, player2

    def __init__(self):
        # display an empty board
        clear()
        player1, player2 = self.setup_game()
        self.play(player1, player2)

# TODO - EXTRA - clear screen after an invalid entry. Board and prompts are \
    # redisplayed and the game informs the player why their input was \
    # unacceptable
# TODO - EXTRA - error messages are detailed and include the invalid guess
# TODO - EXTRA - display both the player's boards on the screen showing ships

if __name__ == '__main__':
    Game()
