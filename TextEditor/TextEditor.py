from socket import timeout
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, colorchooser
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from plyer import notification
import os
import time

main = Tk()
main.geometry("1000x600")
main.title("Textobot Text Editor")
main.resizable(0, 0)
icon = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\TextEditor\Textobot.png")
main.iconphoto(False, icon)

menubar = Menu(main)
main.configure(menu=menubar, bg="#8EE5EE")

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

def new_file():
    global loading
    loading = Tk()
    loading.geometry("800x250")
    loading.title("Loading New Text File...")
    loading.resizable(0, 0)

    frame = Frame(loading, height = 150, width = 750, borderwidth = 10, bd=4)
    frame.pack(pady=40)

    global progressbar_newfile
    progressbar_newfile = ttk.Progressbar(frame, orient = HORIZONTAL, length = 700, maximum = 100, mode = 'determinate')
    progressbar_newfile.pack(pady=5)

    global label_progressbar
    label_progressbar = Label(frame, font = ("arial", 12, "bold"))
    label_progressbar.pack(pady=10)

    button_newfile_progress = Button(frame, text = "Load New File", bg = "darkblue", fg = "white", font = ("Rockwell", 15, "bold"), command = lambda: progressbar())
    button_newfile_progress.pack(pady=10)   

def progressbar():
    for i in range(1, 101, 1):
        progressbar_newfile['value']=i
        loading.update_idletasks()
        label_progressbar.config(text=str(i) + "%" + " loaded")
        time.sleep(0.03)
    
    main.destroy()
    loading.destroy()
    
    new = Tk()
    new.geometry("1000x700")
    new.title("*Untitled*")

    menubar1 = Menu(new)
    new.configure(menu=menubar1, bg="#eee")

    notification.notify(title="New File Created",
                        message="The new file has been created.",
                        timeout=5)

    messagebox.showinfo("New File Created", "The new file has been created.")

    file_menu1 = Menu(menubar1, tearoff=False)
    menubar1.add_cascade(label="File", menu=file_menu1)
    file_menu1.add_command(label="New")
    file_menu1.add_command(label="Open")
    file_menu1.add_separator()
    file_menu1.add_command(label="Close", command = lambda: new.destroy())
    
    edit_menu = Menu(menubar1, tearoff=False)
    menubar1.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Cut")
    edit_menu.add_separator()
    edit_menu.add_command(label="Paste")

    option_menu = Menu(menubar1, tearoff=False)
    menubar1.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Change Font")
    option_menu.add_command(label="Change Font Color")

    help_menu = Menu(menubar1, tearoff=False)
    menubar1.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Search Help")
    help_menu.add_separator()
    help_menu.add_command(label="Web Help")

    frametext = Frame(new, height=670, width=990, bg="white")
    frametext.grid(row=0, column=0, padx=5, pady=3)

def open_file():
    pass

image_newfile = ImageTk.PhotoImage(Image.open("F:\\Sri\\Git\\PythonPuzzles\\TextEditor\\New File.png"))
button_newfile = Button(main, image=image_newfile, relief = RIDGE, borderwidth=4, bg="red", command = lambda: new_file())
button_newfile.grid(row=0, column=0, padx=430, pady=20)

label_newfile = Label(main, text = "Create New File☝", relief = FLAT, font = ("Rockwell", 15, "bold"))
label_newfile.grid(row=1, column=0, padx=430)

image_openfile = ImageTk.PhotoImage(Image.open("F:\\Sri\\Git\\PythonPuzzles\\TextEditor\\Open File.png"))
button_openfile = Button(main, image=image_openfile, relief = RIDGE, borderwidth=4, bg="red", command = lambda: open_file())
button_openfile.grid(row=2, column=0, padx=430, pady=35)

label_openfile = Label(main, text = "Open a File☝", relief = FLAT, font = ("Rockwell", 15, "bold"))
label_openfile.grid(row=3, column=0, padx=430)

main.mainloop()