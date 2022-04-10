from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime

#create screen
keyboard = Tk()
keyboard.geometry("970x800")
keyboard.title("Desktop Keyboard")
icon = PhotoImage(file="C:\\Users\\Sri\\Work\\Git\\PythonPuzzles\\DesktopKeyboard\\paint.png")
keyboard.iconphoto(False, icon)

#create time bar
date = datetime.now().strftime("%H:%M")
label_date = Label(keyboard, text = f"Time: {date}", font = ("arial", 18, "bold"))
label_date.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#create string to get values
var = StringVar()
var = Frame(keyboard, bg="red")
entry_var = Entry(keyboard, bg="#eee", textvariable = var, font = ("arial", 40, "bold"))
entry_var.grid(row=0, column=2, columnspan=10, padx=20)

#creating row 1 buttons
button_q = Button(keyboard, bg = "#eee", text = "q", width=4, font=("arial", 20, "bold"))
button_w = Button(keyboard, bg = "#eee", text = "w", width=4, font=("arial", 20, "bold"))
button_e = Button(keyboard, bg = "#eee", text = "e", width=4, font=("arial", 20, "bold"))
button_r = Button(keyboard, bg = "#eee", text = "r", width=4, font=("arial", 20, "bold"))
button_t = Button(keyboard, bg = "#eee", text = "t", width=4, font=("arial", 20, "bold"))
button_y = Button(keyboard, bg = "#eee", text = "y", width=4, font=("arial", 20, "bold"))
button_u = Button(keyboard, bg = "#eee", text = "u", width=4, font=("arial", 20, "bold"))
button_i = Button(keyboard, bg = "#eee", text = "i", width=4, font=("arial", 20, "bold"))
button_o = Button(keyboard, bg = "#eee", text = "o", width=4, font=("arial", 20, "bold"))
button_p = Button(keyboard, bg = "#eee", text = "p", width=4, font=("arial", 20, "bold"))

#positioning row 1 buttons
button_q.grid(row=1, column=0, padx=5, pady=5)
button_w.grid(row=1, column=1, padx=5, pady=5)
button_e.grid(row=1, column=2, padx=5, pady=5)
button_r.grid(row=1, column=3, padx=5, pady=5)
button_t.grid(row=1, column=4, padx=5, pady=5)
button_y.grid(row=1, column=5, padx=5, pady=5)
button_u.grid(row=1, column=6, padx=5, pady=5)
button_i.grid(row=1, column=7, padx=5, pady=5)
button_o.grid(row=1, column=8, padx=5, pady=5)
button_p.grid(row=1, column=9, padx=5, pady=5)

keyboard.mainloop()