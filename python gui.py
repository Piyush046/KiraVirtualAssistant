from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk 









win=Tk()

win.title("Login page")
win.geometry("925x500")
win.configure(bg="white")
win.resizable(FALSE,FALSE)


img=PhotoImage(file="login.png")

Label(win, image=img,bg="white").place(x=50,y=50)


frame=Frame(win,width=350, height=350, bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text="Sign In", fg="blue", bg="white", font=("verdana",23,) )
heading.place(x=100,y=5)

##################--username
user= Entry(frame, width=25,fg='black',border=0,bg='white',font=("verdana",11))
user.place(x=30,y=80)
user.insert(0,'username')

Frame(frame, width=295,height=2,border=0,bg='black').place(x=25,y=107)



code= Entry(frame, width=25,fg='black',border=0,bg='white',font=("verdana",11))
code.place(x=30,y=150)
code.insert(0,'Password')

Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)


##############___________ Functions

def match():
    username=user.get()
    password=code.get()
    if (username=="admin" and password=="Piyush"):



        print('login panel')
        screen=Toplevel(win)
        screen.title("App")
        screen.geometry("925x500+300+200")

        page2=Label(screen,text="WELCOME TO LOGIN PANEL", fg="black", bg="white", font=("verdana",23,) )
        page2.place(x=200,y=5)
        screen.config(bg="white")


    else:
      messagebox.showerror("invalid","Invalid Username and Password")







##############___________button


Button(frame,width=39,pady=7,text='sign in ',bg='blue', fg='white', border=0,command=match).place(x=35,y=204)
label=Label(frame, text="Don't  have an account?", fg='black',bg='white',font=("verdana",9,))
label.place(x=70,y=270)

##############___________Signup-button


sign_up=Button(frame,width=6,text='Sign Up', border=0,bg='white',cursor='hand2', fg='#57a1f8')
sign_up.place(x=220,y=270)
win.mainloop()