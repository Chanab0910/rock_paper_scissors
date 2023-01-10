import tkinter as tk
from tkinter import ttk
from random import randint
import game_objects
from game_objects import Game, PlayerObject, RPS_OBJECTS, RPS_WIN_DICT, ComputerPlayer, HumanPlayer, Player
from functools import partial


class GUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.game = Game()

        self.Title = tk.Label(self, text='Welcome to RPSLS', font=100)
        self.Name = tk.Label(self, text='Enter your name: ')
        self.Name_input = tk.Entry(self)
        self.Name_button = tk.Button(self, text='Press to enter name', command=self.names)
        self.Round_num = tk.Label(self, text='Enter how many rounds you want to play: ')
        values = ['1', '3', '5']
        self.Round_combobox = ttk.Combobox(self, value=values)
        self.Round_combobox.current(0)
        self.Round_combobox.bind("<<ComboboxSelected>>", self.round_amount)
        self.Air = tk.Label(self, text=' ')
        self.Quit = tk.Button(self, text='Quit', command=quit)
        self.Play_Game_Button = tk.Button(self, text='Play Game', command=partial(NewWindow, self))

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=2)
        self.Name.grid(row=1, column=0)
        self.Name_input.grid(row=1, column=1)
        self.Name_button.grid(row=1, column=2)
        self.Round_num.grid(row=2, column=0)
        self.Round_combobox.grid(row=2, column=1)
        self.Air.grid(row=3)
        self.Quit.grid(row=4, column=0)
        self.Play_Game_Button.grid(row=4, column=1)

    def round_amount(self, values):
        self.game.set_max_rounds(int(self.Round_combobox.get()))

    def names(self):
        self.game.add_human_player(self.Name_input.get())


class NewWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller
        self.game = controller.game
        self.game.add_computer_player()
        self.player = self.game.players[0]
        self.computer = self.game.players[1]
        self.report_round = tk.StringVar()
        self.report_score = tk.StringVar()
        self.report_winner = tk.StringVar()
        self.game.current_round = 1

        self.Title = tk.Label(self, text='RPSLS', font=100, fg='red')
        self.Explain_button_press = tk.Label(self, text='Press on the option you would like to play')
        self.Air = tk.Label(self, text=' ')

        self.options_label = tk.Label(self, text='Pick your option')
        options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.Options_combobox = ttk.Combobox(self, value=options)
        self.Options_combobox.current(0)
        self.Options_combobox.bind("<<ComboboxSelected>>", self.choice)

        self.Round = tk.Label(self, textvariable=self.report_round)
        self.count = 1
        self.Computer_chose_this = tk.Label(self, text=' ')

        self.Score = tk.Label(self, textvariable=self.report_score)

        self.Final_score = tk.Label(self, textvariable=self.report_winner)


        self.Quit = tk.Button(self, text='Quit', command=quit)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=3)
        self.Explain_button_press.grid(row=1, columnspan=3)
        self.Air.grid(row=2)
        self.options_label.grid(row=3, column=0)
        self.Options_combobox.grid(row=3, column=1)

        self.Round.grid(row=4, column=0)
        self.Computer_chose_this.grid(row=5, column=0)
        self.Score.grid(row=6, column=0)
        self.Final_score.grid(row=6, column=2)


        self.Quit.grid(row=7, column=0)

    def choice(self, options):

        if self.player.score < self.game.max_rounds or self.computer.score < self.game.max_rounds :
            print(self.player.score)
            self.player.choose_object(self.Options_combobox.get())
            self.computer.choose_object()
            self.game.find_winner()
            self.report_round.set(self.controller.game.report_round())
            self.report_score.set(self.controller.game.report_score())
            self.game.current_round += 1












if __name__ == '__main__':
    root = tk.Tk()
    main_frame = GUI(root)
    main_frame.pack()
    root.mainloop()
