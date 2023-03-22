from tkinter import *
from tkinter import messagebox
import webbrowser
from AppOpener import open as a
from tkinter import font
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk 
import pygame 
from tkVideoPlayer import TkinterVideo


def Speech2Text ():
    

    class App:
        def __init__(self, master):
            self.label = Label(master, text="Press the button and start speaking!", font=("verdana",12,'bold'))
            self.label.pack()
            
            self.button = Button(master, width=20, height=2 ,text="Start", activebackground="red", background="green", command=self.start_recording)
            self.button.pack()
            
            self.text = Text(master)
            self.text.pack()
            
            self.recognizer = sr.Recognizer()
            
        def start_recording(self):
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(audio)
                    self.text.insert(END, '\n'+text+"\n")
                    #save file 
                    with open("text2.txt", "a") as file:
                        file.write(text+'\n')
                        self.text.insert(END, "\nText saved to file successfully!")

                except sr.UnknownValueError:
                    self.text.insert(END, "\n Sorry, I couldn't understand what you said.")
                except sr.RequestError as e:
                    self.text.insert(END, "\n Sorry, an error occurred while processing your request: {}".format(e))

    root = Tk()
    app = App(root)
    root.title("Speech to Text")
    root.mainloop()
Speech2Text()
