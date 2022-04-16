from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
from gtts import gTTS
import os

translator = Tk()
translator.geometry("515x500")
translator.title("Text-To-Speech Converter")
translator.resizable(0, 0)
photo = PhotoImage(file = "F:\Sri\Git\PythonPuzzles\Text-To-Speech\Mic.png")
translator.iconphoto(False, photo)

class text_to_speech():
    def __init__(self):
        text = entry_text.get()
        speech = gTTS(text = text)
        speech.save("Text-to-Speech.mp3")
        os.system("Text-to-Speech.mp3")

class change_lang():
    def __init__(self):
        language = Tk()
        language.geometry("1200x1000")
        language.title("Change Language Settings")
        language.resizable(0, 0)
        #show all the languages
        languages = "'af': 'Afrikaans'\n'ar': 'Arabic'\n'bg': 'Bulgarian'\n'bn': 'Bengali'\n'bs': 'Bosnian'\n'ca': 'Catalan'\n'cs': 'Czech'\n'cy': 'Welsh'\n'da': 'Danish'\n'de': 'German'\n'el': 'Greek'\n'en': 'English'\n'eo': 'Esperanto'\n'es': 'Spanish'\n'et': 'Estonian'\n'fi': 'Finnish'\n'fr': 'French'\n'gu': 'Gujarati'\n'hi': 'Hindi'\n'hr': 'Croatian'\n'hu': 'Hungarian'\n'hy': 'Armenian'\n'id': 'Indonesian'\n'is': 'Icelandic'\n'it': 'Italian'\n'iw': 'Hebrew'\n'ja': 'Japanese'\n'jw': 'Javanese'\n'km': 'Khmer'\n'kn': 'Kannada'\n'ko': 'Korean'\n'la': 'Latin'\n'lv': 'Latvian'\n'mk': 'Macedonian'\n'ms': 'Malay'\n'ml': 'Malayalam'\n'mr': 'Marathi'\n'my': 'Myanmar (Burmese)'\n'ne': 'Nepali'\n'nl': 'Dutch'\n'no': 'Norwegian'\n'pl': 'Polish'\n'pt': 'Portuguese'\n'ro': 'Romanian'\n'ru': 'Russian'\n'si': 'Sinhala'\n'sk': 'Slovak'\n'sq': 'Albanian'\n'sr': 'Serbian'\n'su': 'Sundanese'\n'sv': 'Swedish'\n'sw': 'Swahili'\n'ta': 'Tamil'\n'te': 'Telugu'\n'th': 'Thai'\n'tl': 'Filipino'\n'tr': 'Turkish'\n'uk': 'Ukrainian'\n'ur': 'Urdu'\n'vi': 'Vietnamese'\n'zh-CN': 'Chinese'\n'zh-TW': 'Chinese (Mandarin/Taiwan)'\n'zh': 'Chinese (Mandarin)'"
        #create scrollbar
        
        #
        label_do = Label(language, text = "Choose the language - To change the language type the language's code in the language entry box.", font = ("Rockwell", 15, "bold"))
        label_do.pack(padx=16, pady=10)
        #
        label_langs = Label(language, text = languages, font = ("Rockwell", 15, "bold"))
        label_langs.pack(padx=16, pady=10)
class open_audio():
    def __init__(self):
        os.system("Text-to-Speech.mp3")

#menu bar 
menu_bar = Menu(translator)
translator.configure(menu = menu_bar)

open_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Open", menu = open_menu)
open_menu.add_command(label = "Open Audio File", command = lambda: open_audio())
open_menu.add_separator()
open_menu.add_command(label = "Make Entered Text as Text File")

close_menu = Menu(menu_bar, tearoff = False)
menu_bar.add_cascade(label = "Close", menu = close_menu)
close_menu.add_command(label = "Close", command = lambda: translator.destroy())

#screen components
label_info = Label(translator, text = "Enter the text that you want to convert to speech:", font = ("Rockwell", 15, "bold"))
label_info.grid(row=0, column=0, padx=15, pady=15)

entry_text = Entry(translator, width=30, font = ("Rockwell", 18, "italic"))
entry_text.grid(row=1, column=0, padx=15, pady=15, columnspan=4)

button_enter = Button(translator, text = "Change text to speech", font = ("Rockwell", 15, "bold"), command = lambda: text_to_speech())
button_enter.grid(row=2, column=0, padx=15, pady=15)

button_change_lang = Button(translator, text = "Change Language Settings", font = ("Rockwell", 15, "bold"), command = lambda: change_lang())
button_change_lang.grid(row=3, column=0, padx=15, pady=10)

image = ImageTk.PhotoImage(Image.open("F:\\Sri\\Git\\PythonPuzzles\\Text-To-Speech\\text-to-speech.png"))
label_image = Label(translator, image=image, relief = RIDGE, borderwidth=6, bg = "blue")
label_image.grid(row=4, column=0, padx=15, pady=15)

translator.mainloop()