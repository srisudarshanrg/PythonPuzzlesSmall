from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime

#create screen
keyboard = Tk()
keyboard.geometry("1000x800")
keyboard.title("Desktop Keyboard")
icon = PhotoImage(file="C:\\Users\\Sri\\Work\\Git\\PythonPuzzles\\DesktopKeyboard\\paint.png")
keyboard.iconphoto(False, icon)

#create time bar
date = datetime.now().strftime("%H:%M")
label_date = Label(keyboard, text = f"Time: {date}", font = ("arial", 18, "bold"))
label_date.grid(row=0, column=0, padx=5, pady=5)

#create string to get values
var = StringVar()
var = Frame(keyboard, bg="red")
entry_var = Entry(keyboard, bg="#eee", textvariable = var, font = ("arial", 50, "bold"))
entry_var.grid(row=0, column=2, columnspan=10, padx=20)

keyboard.mainloop()