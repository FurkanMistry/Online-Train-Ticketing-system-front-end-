#Make sure you run the program from signup.py
from tkinter import *
import main as s

def endpage():
    op = Tk()
    op.geometry("1350x660+0+0")
    op.title("Train Ticket")
    op.configure(background='brown')



    Tops = Frame(op, width = 900, height = 700, bd=16, relief ="raise")
    Tops.pack(side=TOP)
    Tops.grid(pady = (150,0))


    Tops1 = Frame(op, width = 900, height = 700, bd=16, relief ="raise")
    Tops1.grid(pady = (10,10))




    Tops.configure(background='black')
    Tops1.configure(background='black')
    Title = Label(Tops, font=('arial',35), text="Thank you for Booking your tickets from our application.",  height=2,width = 49, bd=6)
    Title.grid(row=0,column=0,sticky=W)
    b = Label(Tops1, font=('arial',35), text="Click Below to book more tickers",  height=1,width = 30, bd=6)
    b.grid(row=1,column=0,sticky=W)



    Print = Button(op, font=('arial', 20, 'bold'), text='        Main Page', bd=16, anchor='w', width=16,fg = 'white',relief='raise', command=s.main)
    Print.grid(row=2, column=0)
    Print.configure(background='black')

    op.mainloop()

