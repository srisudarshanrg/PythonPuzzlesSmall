from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
from gtts import gTTS

translator = Tk()
translator.geometry("500x500")
translator.title("Text-To-Speech Converter")
translator.resizable(0, 0)
photo = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\Text-To-Speech\Mic.png")
translator.iconphoto(False, photo)

class open_audio():
    def __init__(self):
        pass

#menu bar 
menu_bar = Menu(translator)
translator.configure(menu = menu_bar)

open_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Open", menu = open_menu)
open_menu.add_command(label = "Open Audio File", command = open_audio())
open_menu.add_separator()
open_menu.add_command(label = "Make Entered Text as Text File")

close_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Close", menu = close_menu)
close_menu.add_command(label = "Close", command = lambda: translator.destroy())

translator.mainloop()