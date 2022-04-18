from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from plyer import notification
import os
import time

main = Tk()
main.geometry("1000x600")
main.title("Textobot Text Editor")
icon = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\TextEditor\Textobot.png")
main.iconphoto(False, icon)

menubar = Menu(main)
main.configure(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File")
file_menu.add_command(label="Open File")
file_menu.add_separator()
file_menu.add_command(label="Close Window")

help_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Search Help")
help_menu.add_separator()
help_menu.add_command(label="Web Help")

close_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Close", menu=close_menu)
close_menu.add_command(label="Close Window", command=lambda: main.destroy())

image_newfile = ImageTk.PhotoImage(Image.open("F:\\Sri\\Git\\PythonPuzzles\\TextEditor\\New File.png"))
button_newfile = Button(main, image=image_newfile, relief = RIDGE, borderwidth=4, bg="red")
button_newfile.grid(row=0, column=0, padx=430, pady=20)

label_newfile = Label(main, text = "Create New File☝", relief = FLAT, font = ("Rockwell", 15, "bold"))
label_newfile.grid(row=1, column=0, padx=430)

image_openfile = ImageTk.PhotoImage(Image.open("F:\\Sri\\Git\\PythonPuzzles\\TextEditor\\Open File.png"))
button_openfile = Button(main, image=image_openfile, relief = RIDGE, borderwidth=4, bg="red")
button_openfile.grid(row=2, column=0, padx=430, pady=35)

label_openfile = Label(main, text = "Open a File ☝", relief = FLAT, font = ("Rockwell", 15, "bold"))
label_openfile.grid(row=3, column=0, padx=430)

main.mainloop()