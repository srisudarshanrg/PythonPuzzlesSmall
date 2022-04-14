from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
import os

img_dir = os.getcwd()

game = Tk()
game.geometry("700x700")
game.title("Rock Paper Scissors")
photo = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\RockPaperScissors\Scissors.png")
game.iconphoto(False, photo)


game.mainloop()