from tkinter import *
from gtts import gTTS
from plyer import notification

root = Tk()
root.geometry("500x500")
root.title("Convert Text to Speech")

button = Button(root, text = "duh")
button.grid(row=0, column=0, padx=5, pady=5)

message = "me"
title = "duh"
notification.notify(title = title,
                    message = message,
                    timeout = 10)