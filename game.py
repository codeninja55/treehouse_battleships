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

    def validate_guess(self, guess):
        # TODO - validate guess
        # TODO - display guess results
        pass

    def play(self, player1, player2):
        # while self.game_progress():
        # self.first_player_turn()
        # self.second_player_turn()
        # TODO - allow players to take turns

    def setup_game(self):
        # Instantiate two players, ask for name, then place ships
        name1 = input("\nPLAYER 1 NAME > ").lstrip().rstrip().lower()
        name2 = input("\nPLAYER 2 NAME > ").lstrip().rstrip().lower()

        player1 = Player(name1, 1)
        player1.ship_placement()

        while True:
            inp = input("\nPress enter/return when you are ready to "
                        "proceed > ")
            if inp == "":
                break

        # player2 = Player(name2, 2)
        # player2.ship_placement()
        return player1, player2

        while True:
            inp = input("\nPress enter/return when you are ready to begin "
                        "the game > ")
            if inp == "":
                break

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
