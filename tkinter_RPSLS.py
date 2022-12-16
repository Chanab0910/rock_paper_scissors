import tkinter as tk
from tkinter import ttk
from game_object import Game, PlayerObject, RPS_OBJECTS, RPS_WIN_DICT
from functools import partial



class GUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Title = tk.Label(self, text='Welcome to RPSLS', font=100)
        self.Name = tk.Label(self, text='Enter your name: ')
        self.Name_input = tk.Entry(self)
        self.Round_num = tk.Label(self, text='Enter how many rounds you want to play: ')
        s = tk.StringVar()
        values = ['1', '1', '2', '3', '4', '5']
        self.Round_combobox = ttk.OptionMenu(self, s, *values)
        self.Air = tk.Label(self, text=' ')
        self.Quit = tk.Button(self, text='Quit', command=quit)
        self.Play_Game_Button = tk.Button(self, text='Play Game', command=partial(NewWindow, self))
        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=2)
        self.Name.grid(row=1, column=0)
        self.Name_input.grid(row=1, column=1)
        self.Round_num.grid(row=2, column=0)
        self.Round_combobox.grid(row=2, column=1)
        self.Air.grid(row=3)
        self.Quit.grid(row=4, column=0)
        self.Play_Game_Button.grid(row=4, column=1)

class NewWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__(controller)
        self.Title = tk.Label(self, text='RPSLS', font=100, fg='red')
        self.Explain_button_press = tk.Label(self, text='Press on the option you would like to play')
        self.Air = tk.Label(self, text=' ')
        self.Rock_button = tk.Button(self, text='Rock')
        self.Paper_button = tk.Button(self, text='Paper')
        self.Scissor_button = tk.Button(self, text='Scissors')


        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=3)
        self.Explain_button_press.grid(row=1, columnspan=3)
        self.Air.grid(row=2)
        self.Rock_button.grid(row=3, column=0)
        self.Paper_button.grid(row=3, column=1)
        self.Scissor_button.grid(row=3, column=2)





if __name__ == '__main__':
    root = tk.Tk()
    main_frame = GUI(root)
    main_frame.pack()
    root.mainloop()
