from board import Board
from player import Player

class Game:
    def game_progress(self):
        # check if each player still has a ship on the board
        # if a player guess has completely destroyed a ship
            # end game
            # return a false
            # TODO - declare a winner
        # else
            # return true so game can continue
        pass

    def validate_guess(self):
        # TODO - validate guess
        # TODO - display guess results
        pass

    def validate_input(self):
        # TODO - validate user input
        # if user input invalid, rerun the prompt

        # Be as accepting as possible of input. For example, spaces before or
        # after the player’s input is allowed. Both lower and uppercase
        # characters are also allowed. In order to reduce confusion, you may
        # want to clear the screen and display the screen again before each
        # attempt.
        pass

    def second_player_guess(self):
        # TODO - prompt player for guess
        # run validate_input to validate guesses
        # hold a list of guesses to be displayed
        # guess_list = []
        pass

    def first_player_guess(self):
        # TODO - prompt player for guess
        # run validate_input to validate guesses
        # hold a list of guesses to be displayed
        # guess_list = []
        pass

    def __init__(self):
        # TODO - display an empty board

        empty_board = Board()
        empty_board.clear_screen()
        empty_board.print_board()

        # while self.game_progress():
            # self.first_player_turn()
            # self.second_player_turn()
            # TODO - update the board
            # TODO - allow players to take turns
        pass

# TODO - EXTRA - clear screen after an invalid entry. Board and prompts are \
    # redisplayed and the game informs the player why their input was \
    # unacceptable
# TODO - EXTRA - error messages are detailed and include the invalid guess
# TODO - EXTRA - display both the player's boards on the screen showing ships


if __name__ == '__main__':
    Game()
