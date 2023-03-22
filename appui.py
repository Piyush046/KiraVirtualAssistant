from tkinter import *
from tkinter import messagebox
import webbrowser
from AppOpener import open
from tkinter import font
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk 
import pygame 
from tkVideoPlayer import TkinterVideo


#Pygame music library---------------------------------------------------------------------------------

pygame.mixer.init() 
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)



#Translation function-------------------------------------------------------------------------------
def trans():
    global tras_pg
    tras_pg=Tk() 
    tras_pg.title("Translator!!")
    tras_pg.geometry("925x500")
    tras_pg.resizable(FALSE,FALSE)

    #heading Of language translator---------------------------------------------------------------------------

    Label(tras_pg, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", fg='blue', bg='white smoke').pack()
    Label(tras_pg,text ="It’s going to be interesting to see how society deals with artificial intelligence, but it will definitely be cool.”", fg='blue',font = 'arial 10 bold', bg ='white smoke' , width = '200').pack(side = 'bottom')
    
    #INPUT AND OUTPUT TEXT WIDGET-------------------------------------------------------------------------
    Label(tras_pg,text="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
    
    global Input_text
    Input_text = Text(tras_pg,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
    Input_text.place(x=30,y = 100)  
  
    Label(tras_pg,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=600,y=60)
    global Output_text
    Output_text = Text(tras_pg,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
    Output_text.place(x = 500 , y = 100)

    language = list(LANGUAGES.values())

    global src_lang
    src_lang = ttk.Combobox(tras_pg, values= language, width =22)
    src_lang.place(x=20,y=60)
    src_lang.set('choose input language')

    global dest_lang
    dest_lang = ttk.Combobox(tras_pg, values= language, width =22)
    dest_lang.place(x=700,y=60)
    dest_lang.set('choose output language')

   



    def Translate():
        translator = Translator()
        translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    
   
    trans_btn = Button(tras_pg, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
    trans_btn.place(x = 450, y = 380)
    tras_pg.mainloop()
 




#Speech to text function--------------------------------------------------------
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

#Command line function ---------------------------------------------------------------------------------------------------
def cmd ():
    

    class App:
        def __init__(self, master):
            self.label = Label(master, text="Welcome to Kira! Commands", font=("verdana",12,'bold'))
            self.label.pack()
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
                    if text== "youtube.com":
                        webbrowser.open_new("https://"+text)
                    elif text== "google.com":
                        webbrowser.open_new("https://"+text)
                     
                      
                    elif text== "wikipedia.com":
                        webbrowser.open_new("https://"+text)
                    else:
                        webbrowser.open_new("https://www.google.com/search?q="+text)
                        open(text)
                         
                        
                   
                except sr.UnknownValueError:
                    self.text.insert(END, "\n Sorry, I couldn't understand what you said.")
                except sr.RequestError as e:
                    self.text.insert(END, "\n Sorry, an error occurred while processing your request: {}".format(e))

    root1 = Tk()
    app = App(root1)
    root1.title("command")
    root1.mainloop()





#-------------------main function-----------------------------------------------------------------------------------------
    
win=Tk()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()
        pygame.mixer.music.stop()


win.title("Kira!!")
win.geometry("925x500")
win.configure(bg="white")
win.resizable(FALSE,FALSE)
myFont = font.Font(family='Courier',)
win.protocol("WM_DELETE_WINDOW", on_closing)
videoplayer = TkinterVideo(win, scaled=False)
videoplayer.load(r"3.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play()




# --------Function to pause or resume playing the background music------------------------
def music():
    
    pygame.mixer.music.pause()

# img=PhotoImage(file="login1.png")

#Label(win, image=img,bg="white").pack()


frame=Frame(win,width=350, height=350, bg="white")
 
frame.place(x=500,y=70)

frame_txt=Frame(win,width=350, height=60, bg="white")

frame_txt.place(x=500,y=350)
l1=Label(text="Developed By Piyush Pandey ").pack()




heading=Label(frame,text="Kira the Assistant", fg="blue", bg="white", font=("verdana",23,) )
heading.place(x=40,y=5)

Button(frame,width=30,pady=7,text='Speech2Text ',bg='blue',font= ("verdana",10,'bold'), fg='white', border=0,command=Speech2Text).place(x=35,y=204)
Button(frame,width=30,pady=7,text='Translator ',bg='blue',font= ("verdana",10,'bold'), fg='white', border=0,command=trans).place(x=35,y=150)
Button(frame,width=30,pady=7,text='Command ',bg='blue',font= ("verdana",10,'bold'), fg='white', border=0,command=cmd).place(x=35,y=100)
 
 
 # --------Button pause or play the music--------
button_playMusic = Button(win, text='Mute', relief='flat', fg='white', bg='blue',\
                                       font='verdana', height=1, width=6, command=music)
button_playMusic.place(relx=0.90, rely=0.01)

win.mainloop()
