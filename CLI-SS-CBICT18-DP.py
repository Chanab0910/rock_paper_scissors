from game_object import Game, PlayerObject, ComputerPlayer


# Command Line Interface - gives prompts to run the game from the Command line
class ClInterface:
    def __init__(self):
        self.game = Game()

    def set_up(self):
        print('welcome to rock-paper-scissors')
        self.player1 = input('do you want player 1 to be a human or computer')


