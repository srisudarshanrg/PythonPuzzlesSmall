from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk
import webbrowser
import os

img_dir = os.getcwd()

root = Tk()
root.geometry("700x300")
root.title("YouTube Video Downloader")
icon = PhotoImage(file = f"{img_dir}\VideoDownloader\YouTube.png")
root.iconphoto(False, icon)

class search():
    def __init__(self):
        video = YouTube(str(entry_search.get()))
        video_download_link = video.streams.first()
        video_download_link.download()
        messagebox.showinfo("Downloaded", "The video has been downloaded successfully.")

class yt_direct():
    def __init__(self):
        yt = "https://www.youtube.com/"
        webbrowser.open(yt)

menu_bar = Menu(root)
root.configure(menu=menu_bar)                                 

search_yt = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Search YouTube", menu = search_yt)
search_yt.add_command(label = "Download directly from YouTube", command = lambda: yt_direct())
search_yt.add_command(label = "Search YouTube with given URL", command = lambda: search())
                                  
close_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Close", menu = close_menu)
close_menu.add_command(label = "Close Window", command = lambda: root.destroy())

label_frame_search = LabelFrame(root, text = "Enter URL")
label_frame_search.grid(row=0, column=0, padx=10, pady=10)

label_search = Label(label_frame_search, text = "Enter URL of Video to Download:", font = ("Rockwell", 16, "bold"))
label_search.grid(row=0, column=0, padx=5, pady=5)

entry_search = Entry(label_frame_search, font = ("Rockwell", 30))
entry_search.grid(row=1, column=0, padx=15, pady=15)

button_search = Button(label_frame_search, text = "Search Video", font = (12), command = lambda: search())
button_search.grid(row=1, column=1, padx=7, pady=7)

button_close = Button(root, text = "Close", font = ("Rockwell", 16, "bold"), command = lambda: root.destroy())
button_close.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()