from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import datetime
from plyer import notification
import os
import time

main = Tk()
main.title("Textobot Home Screen")
main.geometry("1000x800")
icon_main = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\TextEditor\Textobot.png")
main.iconphoto(False, icon_main)

menu_bar = Menu(main)
main.configure(menu=menu_bar)

main.mainloop()