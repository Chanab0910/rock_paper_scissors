import tkinter as tk
from tkinter import ttk
from game_objects import Game, PlayerObject, RPS_OBJECTS, RPS_WIN_DICT, ComputerPlayer
from functools import partial


class GUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.game = create_game()

        self.Title = tk.Label(self, text='Welcome to RPSLS', font=100)
        self.Name = tk.Label(self, text='Enter your name: ')
        self.Name_input = tk.Entry(self)
        self.Name_button = tk.Button(self, text='Press to enter name', command=self.names)
        self.Round_num = tk.Label(self, text='Enter how many rounds you want to play: ')
        values = ['1','2', '3', '4', '5']
        self.Round_combobox = ttk.Combobox(self, value=values)
        self.Round_combobox.current(0)
        self.Round_combobox.bind("<<ComboboxSelected>>", self.round_amount)
        self.Air = tk.Label(self, text=' ')
        self.Quit = tk.Button(self, text='Quit', command=quit)
        self.Play_Game_Button = tk.Button(self, text='Play Game', command=partial(NewWindow, self))

        self.game.add_human_player(self.Name_input.get())
        self.game.add_computer_player()

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
        self.mr = self.Round_combobox.get()

    def names(self):
        self.name = self.Name_input.get()


class NewWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__(controller)

        self.controller = controller
        self.game = controller.game
        self.player = self.game.players[0]
        self.computer = self.game.players[1]

        self.Title = tk.Label(self, text='RPSLS', font=100, fg='red')
        self.Explain_button_press = tk.Label(self, text='Press on the option you would like to play')
        self.Air = tk.Label(self, text=' ')
        self.Rock_button = tk.Button(self, text='Rock', command=self.rock_choice)
        self.Paper_button = tk.Button(self, text='Paper', command=self.paper_choice)
        self.Scissor_button = tk.Button(self, text='Scissors', command=self.scissors_choice)
        self.Round = tk.Label(self, text='Round 1:')
        self.Computer_chose_this = tk.Label(self, text=' ')
        self.Score = tk.Label(self, text='0-0')
        self.Quit = tk.Button(self, text='Quit', command=quit)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=3)
        self.Explain_button_press.grid(row=1, columnspan=3)
        self.Air.grid(row=2)
        self.Rock_button.grid(row=3, column=0)
        self.Paper_button.grid(row=3, column=1)
        self.Scissor_button.grid(row=3, column=2)
        self.Round.grid(row=4, column=0)
        self.Computer_chose_this.grid(row=5, column=0)
        self.Score.grid(row=6, column=0)
        self.Quit.grid(row=7, column=0)

    def rock_choice(self):
        self.player.choose_object('Rock')
        self.Computer_chose_this.config(text=self.controller.game.add_computer_player())

    def paper_choice(self):
        self.player.choose_object('Paper')

    def scissors_choice(self):
        self.player.choose_object('Scissors')


def create_game():
    game = Game()
    return game

if __name__ == '__main__':
    root = tk.Tk()
    main_frame = GUI(root)
    main_frame.pack()
    root.mainloop()
