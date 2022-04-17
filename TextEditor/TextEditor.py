from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from plyer import notification
import os
import time

main = Tk()
main.geometry("1000x800")
main.title("Textobot Text Editor")

button_newfile = Button(main, text="Create New File", font=("Rockwell", 20, "bold"), command=lambda: step())
button_newfile.grid(row=0, column=0, padx=5, pady=5)

progressbar_ = ttk.Progressbar(main, orient=HORIZONTAL, length=300, mode='determinate')
progressbar_.grid(row=1, column=0, padx=5, pady=5)

def step():
    for x in range(5):
        progressbar_['value'] += 20
        x+=1

main.mainloop()