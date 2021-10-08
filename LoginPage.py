#Make sure you run the program from signup.py
from tkinter import *
from tkinter import ttk
import main as d

def go():
    
    window = Tk()
    window.title("LoginPage")
    window.geometry('730x270')
    window.configure(background = "black")

    k = Label(window,font=('arial',20, 'bold'),text = "  LOGIN PAGE ",bg='brown', relief='sunken', bd=8).grid(row = 0,column = 0, pady=(10),padx=(250,0))
    a = Label(window ,font=('arial',20, 'bold'),text = "Email :").grid(row = 1,column = 0,pady=(10))
    b = Label(window ,font=('arial',20, 'bold'),text = "Password :").grid(row = 2,column = 0,pady=(10))
   
    a1 = Entry(window, width=16,  font=('arial', 16, 'bold'))
    a1.grid(row = 1,column = 1)
    b1 = Entry(window, width=16,  font=('arial', 16, 'bold')).grid(row = 2,column = 1)
   
    
    btn = Button(window,font=('arial',12, 'bold'),text = " Login ",bg='brown', relief='raise', bd=8, command=d.main).grid(row=3,column=1)
    
    window.mainloop()
    