from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import datetime
import os
import webbrowser
import time

#create screen
keyboard = Tk()
keyboard.geometry("930x585")
keyboard.title("Desktop Keyboard")
keyboard.resizable(0, 0)
menu_bar = Menu(keyboard)
keyboard.configure(bg="skyblue", menu=menu_bar)

img_dir = os.getcwd()

icon = PhotoImage(file=f"{img_dir}\DesktopKeyboard\paint.png")
keyboard.iconphoto(False, icon)

#create functions for the buttons   
def letters(item):
    global expression
    expression = expression + str(item)
    var.set(expression)

def letter_clear():
    global expression
    expression = ""
    var.set("")

def tab():
    global expression
    expression = expression + "\t"
    var.set(expression)

def space():
    global expression
    expression = expression + " "
    var.set(expression)

def caps():
    global expression
    expression = expression.upper()
    var.set(expression)

def calculate():
    global expression
    expression = str(eval(expression))
    try:
        var.set(expression)
    except ValueError:
        messagebox.showerror("Value Invalid", "For calculation please enter an integer value.")
    except NameError:
        messagebox.showerror("Value Invalid", "For calculation please enter an integer value.")

def help():
    #create screen
    global img_dir
    global root
    root = Tk()
    root.geometry("1100x700")
    root.title("Help")
    menu_help = Menu(root)
    root.configure(bg="#FF6103", menu=menu_help)
    #create menu bar
    close_menu = Menu(menu_help, tearoff = False)
    menu_help.add_cascade(label = "Close", menu = close_menu)
    close_menu.add_command(label = "Close Help Window", command = lambda: root.destroy())
    close_menu.add_command(label = "Close Entire Application", command = lambda: exit())
    #create help frame
    global entry_help
    global button_help
    help_frame = LabelFrame(root, text = "Enter what help you need:")
    help_frame.grid(row=1, column=1, padx=20, pady=10)
    entry_help = Entry(help_frame, font = ("arial", 30, "bold"))
    entry_help.grid(row=1, column=1, padx=5, pady=5)
    button_help = Button(help_frame, text = "Search Help", command = lambda: help_box())
    button_help.grid(row=1, column=2, padx=5, pady=3)
    #create text box
    global text_help
    text_help = Label(root, font = ("Calibri", 20, "bold"), width = 75, height = 15, wraplength=1000)
    text_help.grid(row=2, column=1, padx=20, pady=20)
    #create a close button
    button_close = Button(root, text = "Close..", font = (35), command = lambda: root.destroy())
    button_close.grid(row=3, column=1, padx=20, pady=5)

def help_box():
    entry_search = entry_help.get().lower()
    if "how to use" in entry_search:
        answer = "- To enter a value into the entry space, just click on the button and it will be reflected on the entry space."
        text_help.configure(text = answer)

expression = ""        

#create function for web help: menu bar; help menu; web search: line 33
class web_help():
    def __init__(self):
        website = "https://support.microsoft.com/en-us/windows/use-the-on-screen-keyboard-osk-to-type-ecbb5e08-5b4e-d8c8-f794-81dbf896267a#:~:text=Go%20to%20Start%20%2C%20then%20select%20Settings%20%3E%20Ease%20of%20Access%20%3E,screen%20until%20you%20close%20it."
        webbrowser.open(website)

#create menu bar
edit_menu = Menu(menu_bar, tearoff=False)   #menu bar already created at the starting: line 10; line 11
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_separator()
edit_menu.add_command(label="Paste")
edit_menu.configure(bg="skyblue")

help_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Search Help", command = lambda: help())
help_menu.add_separator()
help_menu.add_command(label="Web Help", command = lambda: web_help())
help_menu.configure(bg="DodgerBlue2")

keyboard_close_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Close", menu = keyboard_close_menu)
keyboard_close_menu.add_command(label = "Close Application", command = lambda: exit())

#create time bar
date = datetime.now().strftime("%H:%M")
label_date = Label(keyboard, text = f"Time: {date}", font = ("arial", 18, "bold"))
label_date.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#create string to get values
var = StringVar()
var_frame = Frame(keyboard)
entry_var = Entry(keyboard, textvariable = var, fg = "black", font = ("arial", 35, "bold"), justify = LEFT)
entry_var.grid(row=0, column=2, columnspan=10, padx=20, pady=5)

#creating row 1 buttons
button_q = Button(keyboard, bg = "#eee", text = "q", width=4, font=("arial", 20, "bold"), command = lambda: letters("q"))
button_w = Button(keyboard, bg = "#eee", text = "w", width=4, font=("arial", 20, "bold"), command = lambda: letters("w"))
button_e = Button(keyboard, bg = "#eee", text = "e", width=4, font=("arial", 20, "bold"), command = lambda: letters("e"))
button_r = Button(keyboard, bg = "#eee", text = "r", width=4, font=("arial", 20, "bold"), command = lambda: letters("r"))
button_t = Button(keyboard, bg = "#eee", text = "t", width=4, font=("arial", 20, "bold"), command = lambda: letters("t"))
button_y = Button(keyboard, bg = "#eee", text = "y", width=4, font=("arial", 20, "bold"), command = lambda: letters("y"))
button_u = Button(keyboard, bg = "#eee", text = "u", width=4, font=("arial", 20, "bold"), command = lambda: letters("u"))
button_i = Button(keyboard, bg = "#eee", text = "i", width=4, font=("arial", 20, "bold"), command = lambda: letters("i"))
button_o = Button(keyboard, bg = "#eee", text = "o", width=4, font=("arial", 20, "bold"), command = lambda: letters("o"))
button_p = Button(keyboard, bg = "#eee", text = "p", width=4, font=("arial", 20, "bold"), command = lambda: letters("p"))

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
caps_lock = PhotoImage(file=f"{img_dir}\DesktopKeyboard\caps_lock.png")
button_caps = Button(keyboard, bg="#eee", image = caps_lock, command = lambda: caps())
button_a = Button(keyboard, bg = "#eee", text = "a", width=4, font=("arial", 20, "bold"), command = lambda: letters("a"))
button_s = Button(keyboard, bg = "#eee", text = "s", width=4, font=("arial", 20, "bold"), command = lambda: letters("s"))
button_d = Button(keyboard, bg = "#eee", text = "d", width=4, font=("arial", 20, "bold"), command = lambda: letters("d"))
button_f = Button(keyboard, bg = "#eee", text = "f", width=4, font=("arial", 20, "bold"), command = lambda: letters("f"))
button_g = Button(keyboard, bg = "#eee", text = "g", width=4, font=("arial", 20, "bold"), command = lambda: letters("g"))
button_h = Button(keyboard, bg = "#eee", text = "h", width=4, font=("arial", 20, "bold"), command = lambda: letters("h"))
button_j = Button(keyboard, bg = "#eee", text = "j", width=4, font=("arial", 20, "bold"), command = lambda: letters("j"))
button_k = Button(keyboard, bg = "#eee", text = "k", width=4, font=("arial", 20, "bold"), command = lambda: letters("k"))
button_l = Button(keyboard, bg = "#eee", text = "l", width=4, font=("arial", 20, "bold"), command = lambda: letters("l"))

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
button_z = Button(keyboard, bg = "#eee", text = "z", width=4, font=("arial", 20, "bold"), command = lambda: letters("z"))
button_x = Button(keyboard, bg = "#eee", text = "x", width=4, font=("arial", 20, "bold"), command = lambda: letters("x"))
button_c = Button(keyboard, bg = "#eee", text = "c", width=4, font=("arial", 20, "bold"), command = lambda: letters("c"))
button_v = Button(keyboard, bg = "#eee", text = "v", width=4, font=("arial", 20, "bold"), command = lambda: letters("v"))
button_b = Button(keyboard, bg = "#eee", text = "b", width=4, font=("arial", 20, "bold"), command = lambda: letters("b"))
button_n = Button(keyboard, bg = "#eee", text = "n", width=4, font=("arial", 20, "bold"), command = lambda: letters("n"))
button_m = Button(keyboard, bg = "#eee", text = "m", width=4, font=("arial", 20, "bold"), command = lambda: letters("m"))
button_enter = Button(keyboard, bg = "#eee", text = "Tab", width=4, font=("arial", 20, "bold"), command = lambda: tab())
button_stop = Button(keyboard, bg = "#eee", text = ".", width=4, font=("arial", 20, "bold"), command = lambda: letters("."))

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
button_semicolon = Button(keyboard, bg = "#eee", text = ";", width = 4, font = ("arial", 20, "bold"), command = lambda: letters(";"))
button_colon = Button(keyboard, bg = "#eee", text = ":", width = 4, font = ("arial", 20, "bold"), command = lambda: letters(":"))
button_quote = Button(keyboard, bg = "#eee", text = "'", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("'"))
button_doubleqoute = Button(keyboard, bg = "#eee", text = "''", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("''"))
button_qmark = Button(keyboard, bg = "#eee", text = "?", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("?"))
button_slash = Button(keyboard, bg = "#eee", text = "/", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("/"))
button_reverseslash = Button(keyboard, bg = "#eee", text = "\ ", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("\ "))
button_at = Button(keyboard, bg = "#eee", text = "@", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("@"))
button_hash = Button(keyboard, bg = "#eee", text = "#", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("#"))
button_and = Button(keyboard, bg = "#eee", text = "&", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("&"))

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
button_add = Button(keyboard, bg = "#eee", text = "+", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("+"))
button_sub = Button(keyboard, bg = "#eee", text = "-", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("-"))
button_mply = Button(keyboard, bg = "#eee", text = "*", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("*"))
button_dvd = Button(keyboard, bg = "#eee", text = "/", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("/"))
button_equal2 = Button(keyboard, bg = "#eee", text = "=", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("="))
button_brc1 = Button(keyboard, bg = "#eee", text = "()", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("()"))
button_brc2 = Button(keyboard, bg = "#eee", text = "{}", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("{}"))
button_brc3 = Button(keyboard, bg = "#eee", text = "[]", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("[]"))
button_per = Button(keyboard, bg = "#eee", text = "%", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("%"))
button_equal = Button(keyboard, bg = "#eee", text = "==", width = 4, font = ("arial", 20, "bold"), command = lambda: calculate())

#positioning row 5 buttons
button_add.grid(row=5, column=0, padx=5, pady=5)
button_sub.grid(row=5, column=1, padx=5, pady=5)
button_mply.grid(row=5, column=2, padx=5, pady=5)
button_dvd.grid(row=5, column=3, padx=5, pady=5)
button_equal2.grid(row=5, column=4, padx=5, pady=5)
button_brc1.grid(row=5, column=5, padx=5, pady=5)
button_brc2.grid(row=5, column=6, padx=5, pady=5)
button_brc3.grid(row=5, column=7, padx=5, pady=5)
button_per.grid(row=5, column=8, padx=5, pady=5)
button_equal.grid(row=5, column=9, padx=5, pady=5)

#creating row 6 buttons - numbers
button_1 = Button(keyboard, bg = "#eee", text = "1", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("1"))
button_2 = Button(keyboard, bg = "#eee", text = "2", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("2"))
button_3 = Button(keyboard, bg = "#eee", text = "3", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("3"))
button_4 = Button(keyboard, bg = "#eee", text = "4", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("4"))
button_5 = Button(keyboard, bg = "#eee", text = "5", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("5"))
button_6 = Button(keyboard, bg = "#eee", text = "6", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("6"))
button_7 = Button(keyboard, bg = "#eee", text = "7", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("7"))
button_8 = Button(keyboard, bg = "#eee", text = "8", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("8"))
button_9 = Button(keyboard, bg = "#eee", text = "9", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("9"))
button_0 = Button(keyboard, bg = "#eee", text = "0", width = 4, font = ("arial", 20, "bold"), command = lambda: letters("0"))

#positioning row 6 buttons
button_1.grid(row=6, column=0, padx=5, pady=5)
button_2.grid(row=6, column=1, padx=5, pady=5)
button_3.grid(row=6, column=2, padx=5, pady=5)
button_4.grid(row=6, column=3, padx=5, pady=5)
button_5.grid(row=6, column=4, padx=5, pady=5)
button_6.grid(row=6, column=5, padx=5, pady=5)
button_7.grid(row=6, column=6, padx=5, pady=5)
button_8.grid(row=6, column=7, padx=5, pady=5)
button_9.grid(row=6, column=8, padx=5, pady=5)
button_0.grid(row=6, column=9, padx=5, pady=5)

#creating row 7 buttons
button_ctrl = Button(keyboard, bg = "#eee", text = "Ctrl", width = 9, font = ("arial", 20, "bold"))
button_space = Button(keyboard, bg = "#eee", text = "Space", width=25, font = ("arial", 20, "bold"), command = lambda: space())
button_alt = Button(keyboard, bg = "#eee", text = "Alt", width = 4, font = ("arial", 20, "bold"))
button_clear = Button(keyboard, bg = "#eee", text = "Clear All", width = 8, font = ("arial", 20, "bold"), command = lambda: letter_clear())

#positioning row 7 buttons
button_ctrl.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
button_space.grid(row=7, column=2, columnspan=5, padx=5, pady=5)
button_alt.grid(row=7, column=9, padx=5, pady=5)
button_clear.grid(row=7, column=7, columnspan=2, padx=5, pady=5)

keyboard.mainloop()     