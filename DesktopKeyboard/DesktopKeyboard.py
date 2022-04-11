from tkinter import *
from PIL import Image,ImageTk
import os
from datetime import datetime

#create screen
keyboard = Tk()
keyboard.geometry("970x800")
keyboard.title("Desktop Keyboard")
keyboard.configure(bg="skyblue")

img_dir = os.getcwd()

icon = PhotoImage(file=f"{img_dir}\DesktopKeyboard\paint.png")
keyboard.iconphoto(False, icon)

#create time bar
date = datetime.now().strftime("%H:%M")
label_date = Label(keyboard, text = f"Time: {date}", font = ("arial", 18, "bold"))
label_date.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#create string to get values
var = StringVar()
var = Frame(keyboard, bg="red")
entry_var = Entry(keyboard, textvariable = var, bg = "cyan", fg = "black", font = ("arial", 40, "bold"))
entry_var.grid(row=0, column=2, columnspan=10, padx=20, pady=5)

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

#creating row 2 buttons
caps = PhotoImage(file=f"{img_dir}\DesktopKeyboard\caps_lock.png")
button_caps = Button(keyboard, bg="#eee", image = caps)
button_a = Button(keyboard, bg = "#eee", text = "a", width=4, font=("arial", 20, "bold"))
button_s = Button(keyboard, bg = "#eee", text = "s", width=4, font=("arial", 20, "bold"))
button_d = Button(keyboard, bg = "#eee", text = "d", width=4, font=("arial", 20, "bold"))
button_f = Button(keyboard, bg = "#eee", text = "f", width=4, font=("arial", 20, "bold"))
button_g = Button(keyboard, bg = "#eee", text = "g", width=4, font=("arial", 20, "bold"))
button_h = Button(keyboard, bg = "#eee", text = "h", width=4, font=("arial", 20, "bold"))
button_j = Button(keyboard, bg = "#eee", text = "j", width=4, font=("arial", 20, "bold"))
button_k = Button(keyboard, bg = "#eee", text = "k", width=4, font=("arial", 20, "bold"))
button_l = Button(keyboard, bg = "#eee", text = "l", width=4, font=("arial", 20, "bold"))

#positioning row 2 buttons
button_caps.grid(row=2, column=0, padx=5, pady=5)
button_a.grid(row=2, column=1, padx=5, pady=5)
button_s.grid(row=2, column=2, padx=5, pady=5)
button_d.grid(row=2, column=3, padx=5, pady=5)
button_f.grid(row=2, column=4, padx=5, pady=5)
button_g.grid(row=2, column=5, padx=5, pady=5)
button_h.grid(row=2, column=6, padx=5, pady=5)
button_j.grid(row=2, column=7, padx=5, pady=5)
button_k.grid(row=2, column=8, padx=5, pady=5)
button_l.grid(row=2, column=9, padx=5, pady=5)

#creating row 3 buttons
button_shift = Button(keyboard, bg = "#eee", text = "Shift", width=4, font=("arial", 20, "bold"))
button_z = Button(keyboard, bg = "#eee", text = "z", width=4, font=("arial", 20, "bold"))
button_x = Button(keyboard, bg = "#eee", text = "x", width=4, font=("arial", 20, "bold"))
button_c = Button(keyboard, bg = "#eee", text = "c", width=4, font=("arial", 20, "bold"))
button_v = Button(keyboard, bg = "#eee", text = "v", width=4, font=("arial", 20, "bold"))
button_b = Button(keyboard, bg = "#eee", text = "b", width=4, font=("arial", 20, "bold"))
button_n = Button(keyboard, bg = "#eee", text = "n", width=4, font=("arial", 20, "bold"))
button_m = Button(keyboard, bg = "#eee", text = "m", width=4, font=("arial", 20, "bold"))
button_enter = Button(keyboard, bg = "#eee", text = "Enter", width=4, font=("arial", 20, "bold"))
button_stop = Button(keyboard, bg = "#eee", text = ".", width=4, font=("arial", 20, "bold"))

#positioning row 3 buttons
button_shift.grid(row=3, column=0, padx=5, pady=5)
button_z.grid(row=3, column=1, padx=5, pady=5)
button_x.grid(row=3, column=2, padx=5, pady=5)
button_c.grid(row=3, column=3, padx=5, pady=5)
button_v.grid(row=3, column=4, padx=5, pady=5)
button_b.grid(row=3, column=5, padx=5, pady=5)
button_n.grid(row=3, column=6, padx=5, pady=5)
button_m.grid(row=3, column=7, padx=5, pady=5)
button_stop.grid(row=3, column=8, padx=5, pady=5)
button_enter.grid(row=3, column=9, padx=5, pady=5)

#creating row 4 buttons
button_semicolon = Button(keyboard, bg = "#eee", text = ";", width = 4, font = ("arial", 20, "bold"))
button_colon = Button(keyboard, bg = "#eee", text = ":", width = 4, font = ("arial", 20, "bold"))
button_quote = Button(keyboard, bg = "#eee", text = "'", width = 4, font = ("arial", 20, "bold"))
button_doubleqoute = Button(keyboard, bg = "#eee", text = "''", width = 4, font = ("arial", 20, "bold"))
button_qmark = Button(keyboard, bg = "#eee", text = "?", width = 4, font = ("arial", 20, "bold"))
button_slash = Button(keyboard, bg = "#eee", text = "/", width = 4, font = ("arial", 20, "bold"))
button_reverseslash = Button(keyboard, bg = "#eee", text = "\ ", width = 4, font = ("arial", 20, "bold"))
button_at = Button(keyboard, bg = "#eee", text = "@", width = 4, font = ("arial", 20, "bold"))
button_hash = Button(keyboard, bg = "#eee", text = "#", width = 4, font = ("arial", 20, "bold"))
button_and = Button(keyboard, bg = "#eee", text = "&", width = 4, font = ("arial", 20, "bold"))

#positioning row 4 buttons
button_semicolon.grid(row=4, column=0, padx=5, pady=5)
button_colon.grid(row=4, column=1, padx=5, pady=5)
button_quote.grid(row=4, column=2, padx=5, pady=5)
button_doubleqoute.grid(row=4, column=3, padx=5, pady=5)
button_qmark.grid(row=4, column=4, padx=5, pady=5)
button_slash.grid(row=4, column=5, padx=5, pady=5)
button_reverseslash.grid(row=4, column=6, padx=5, pady=5)
button_at.grid(row=4, column=7, padx=5, pady=5)
button_hash.grid(row=4, column=8, padx=5, pady=5)
button_and.grid(row=4, column=9, padx=5, pady=5)

keyboard.mainloop()     