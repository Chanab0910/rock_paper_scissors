import tkinter as tk
from tkinter import ttk
from game_object import Game, PlayerObject, RPS_OBJECTS, RPS_WIN_DICT

class GUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, master):
        super().__init__(master)

        self.Title = tk.Label(self, text='Welcome to RPSLS', font=100)
        self.Name = tk.Label(self, text='Enter your name: ')
        self.Name_input = tk.Entry(self)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=2)
        self.Name.grid(row=1, column=0)
        self.Name_input.grid(row=1, column=1)






if __name__ == '__main__':
    root = tk.Tk()
    main_frame = GUI(root)
    main_frame.pack()
    root.mainloop()
