from board import Board
from player import Player
import os

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

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def __init__(self):
        # display an empty board
        self.clear()
        empty_board = Board()
        empty_board.clear_screen()
        empty_board.print_board()

        # Instantiate two players, ask for name, then place ships
        player1 = Player()
        player1.ship_placement()
        # self.clear()
        player2 = Player()
        player2.ship_placement()

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
