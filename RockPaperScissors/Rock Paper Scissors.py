from fileinput import close
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
import os

img_dir = os.getcwd()

#create screen
game = Tk()
game.geometry("700x700")
game.title("Rock Paper Scissors")
photo = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\RockPaperScissors\Scissors.png")
game.iconphoto(False, photo)
menu_bar = Menu(game)
game.configure(bg="skyblue", menu=menu_bar)

user_score = 0
comp_score = 0

class rock():
    def __init__(self):
        pass

class paper():
    def __init__(self):
        pass

class scissors():
    def __init__(self):
        pass

class save_file():
    def __init__(self):
        pass

class open_file():
    def __init__(self):
        pass

class game_close():
    def __init__(self):
        pass

class copy_score():
    def __init__(self):
        pass

class cut_score():
    def __init__(self):
        pass

#create menu bar
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command = lambda: save_file())
file_menu.add_command(label="Open", command = lambda: open_file())
file_menu.add_separator()
file_menu.add_command(label="Close", command = lambda: game_close())

edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command = lambda: copy_score())
edit_menu.add_command(label="Cut", command = lambda: cut_score)

close_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Close", menu=close_menu)
close_menu.add_command(label="Close Window", command = lambda: game.destroy())
close_menu.add_checkbutton(label="Save Scores and Close", command = lambda: game_close())

#create the game labels, buttons and text boxes
label_game = Label(game, text = "Choose:", fg = "blue3", font = ("rockwell", 25, "bold"))
label_game.grid(row=0, column=0, columnspan=2, pady=15)

button_rock = Button(game, text = "Rock", bg="#00C957", relief = "groove", font = ("rockwell", 20, "bold"), command=lambda: rock())
button_rock.grid(row=1, column=0, padx=5, pady=10)

button_paper = Button(game, text = "Paper", bg = "#EEAD0E", relief = "groove", font = ("rockwell", 20, "bold"), command=lambda: paper())
button_paper.grid(row=1, column=1, padx=5, pady=10)

button_scissor = Button(game, text = "Scissors", bg = "#CD2626", relief = "groove", font = ("rockwell", 20, "bold"), command=lambda: scissors())
button_scissor.grid(row=1, column=2, padx=5, pady=10)

label_score = Label(game, bg = "#FFD700", borderwidth=2, relief="groove", fg = "black", width=41, height = 10,  font = ("rockwell", 20))
label_score.grid(row=2, column=0, rowspan=4, columnspan=15, padx=15, pady=7)

label_versus = Label(game, text = "PLAYER           VS           COMPUTER", fg = "blue", font = ("Britannic Bold", 30, "bold"))
label_versus.grid(row=15, column=0, columnspan=15, padx=7, pady=10)

button_close = Button(game, text = "Close", font = ("Rockwell", 18), command=lambda: game.destroy())
button_close.grid(row=16, column=2)

button_close_n_s = Button(game, text = "Save & Close", font = ("Rockwell", 18), command = lambda: game_close())
button_close_n_s.grid(row=17, column=2, pady=8)

game.mainloop()