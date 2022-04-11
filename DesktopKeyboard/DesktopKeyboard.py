from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import os
import webbrowser

#create screen
keyboard = Tk()
keyboard.geometry("960x530")
keyboard.title("Desktop Keyboard")
menu_bar = Menu(keyboard)
keyboard.configure(bg="skyblue", menu=menu_bar)

img_dir = os.getcwd()

icon = PhotoImage(file=f"{img_dir}\DesktopKeyboard\paint.png")
keyboard.iconphoto(False, icon)

#create function for web help: menu bar; help menu; web search: line 33
class web_help():
    def __init__(self):
        website = "https://support.microsoft.com/en-us/windows/use-the-on-screen-keyboard-osk-to-type-ecbb5e08-5b4e-d8c8-f794-81dbf896267a#:~:text=Go%20to%20Start%20%2C%20then%20select%20Settings%20%3E%20Ease%20of%20Access%20%3E,screen%20until%20you%20close%20it."
        webbrowser.open(website)

#create menu bar
edit_menu = Menu(menu_bar)   #menu bar already created at the starting: line 10; line 11
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_separator()
edit_menu.add_command(label="Paste")
edit_menu.configure(bg="skyblue")

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Search Help")
help_menu.add_separator()
help_menu.add_command(label="Web Help", command = lambda: web_help())
help_menu.configure(bg="DodgerBlue2")

#create time bar
date = datetime.now().strftime("%H:%M")
label_date = Label(keyboard, text = f"Time: {date}", font = ("arial", 18, "bold"))
label_date.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#create settings icon
settings_icon = PhotoImage(file = f"{img_dir}\DesktopKeyboard\settings.png")
settings_button = Button(keyboard, image=settings_icon)
settings_button.grid(row=6, column=4, padx=20, pady=5)

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

#creating row 5 buttons
button_add = Button(keyboard, bg = "#eee", text = "+", width = 4, font = ("arial", 20, "bold"))
button_sub = Button(keyboard, bg = "#eee", text = "-", width = 4, font = ("arial", 20, "bold"))
button_mply = Button(keyboard, bg = "#eee", text = "*", width = 4, font = ("arial", 20, "bold"))
button_dvd = Button(keyboard, bg = "#eee", text = "/", width = 4, font = ("arial", 20, "bold"))
button_dlr = Button(keyboard, bg = "#eee", text = "$", width = 4, font = ("arial", 20, "bold"))
button_brc1 = Button(keyboard, bg = "#eee", text = "()", width = 4, font = ("arial", 20, "bold"))
button_brc2 = Button(keyboard, bg = "#eee", text = "{}", width = 4, font = ("arial", 20, "bold"))
button_brc3 = Button(keyboard, bg = "#eee", text = "[]", width = 4, font = ("arial", 20, "bold"))
button_per = Button(keyboard, bg = "#eee", text = "%", width = 4, font = ("arial", 20, "bold"))
button_sh6 = Button(keyboard, bg = "#eee", text = "^", width = 4, font = ("arial", 20, "bold"))

#positioning row 5 buttons
button_add.grid(row=5, column=0, padx=5, pady=5)
button_sub.grid(row=5, column=1, padx=5, pady=5)
button_mply.grid(row=5, column=2, padx=5, pady=5)
button_dvd.grid(row=5, column=3, padx=5, pady=5)
button_dlr.grid(row=5, column=4, padx=5, pady=5)
button_brc1.grid(row=5, column=5, padx=5, pady=5)
button_brc2.grid(row=5, column=6, padx=5, pady=5)
button_brc3.grid(row=5, column=7, padx=5, pady=5)
button_per.grid(row=5, column=8, padx=5, pady=5)
button_sh6.grid(row=5, column=9, padx=5, pady=5)

keyboard.mainloop()     