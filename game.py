from board import Board
from helpers import clear, clear_screen
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
        return True

    def validate_guess(self):
        # TODO - validate guess
        # TODO - display guess results
        pass

    def setup_game(self):
        # Instantiate two players, ask for name, then place ships
        player1 = Player()
        player1.ship_placement()
        # self.clear()
        player2 = Player()
        player2.ship_placement()

    def __init__(self):
        # display an empty board
        clear()
        empty_board = Board()
        clear_screen()
        empty_board.print_board(empty_board.game_board)

        while self.game_progress():
            self.setup_game()
            # self.first_player_turn()
            # self.second_player_turn()
            # TODO - update the board
            # TODO - allow players to take turns


# TODO - EXTRA - clear screen after an invalid entry. Board and prompts are \
    # redisplayed and the game informs the player why their input was \
    # unacceptable
# TODO - EXTRA - error messages are detailed and include the invalid guess
# TODO - EXTRA - display both the player's boards on the screen showing ships


if __name__ == '__main__':
    Game()
