from game_object import PlayerObject, HumanPlayer, ComputerPlayer, Game


class Cli_interface:
    def __init__(self):
        self.game = Game()
        self.name = None

    def set_up(self):
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock")
        num_players = int(input("Enter how many players you would like to add: "))
        while num_players != 1 and num_players != 2:
            num_players = int(input("Enter a number of players that is 1 or 2: "))

        if num_players == 1:
            name = input("Please enter your name: ")
            self.game.add_human_player(name)
            self.game.add_computer_player()
        elif num_players == 2:
            name1 = input("Please enter your name for Player 1: ")
            name2 = input("Please enter your name for Player 2: ")
            self.game.add_human_player(name1)
            self.game.add_human_player(name2)
        self.input_max_rounds()

    def input_max_rounds(self):
        self.game.set_max_rounds(int(input("What is the maximum number of rounds? ")))

    def get_choices(self):
        for player in self.game.players:
            if player.name != "Computer":
                choice = input(f"{player.name} what move would you like to play: ")
                while choice != "Rock" and choice != "Paper" and choice != "Lizard" and choice != "Scissors" and choice != "Spock":
                    choice = input("Enter a move from (Rock, Paper, Lizard, Scissors, Spock")
                player.choose_object(choice)
            else:
                player.choose_object()

    def run_game(self):
        while not self.game.is_finished():
            self.get_choices()
            self.game.find_winner()
            print(self.game.report_round())
            print(self.game.report_score())
            self.game.next_round()
        print("Game over")
        print(self.game.report_winner())

    def run_sequence(self):
        self.set_up()
        self.run_game()





if __name__ == "__main__":
    cli = Cli_interface()
    cli.run_sequence()