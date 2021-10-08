#          PYTHON PROJECT BY FIT032 MOHAMMED FURKAN MISTRY
#                                   AND
#                        FIT051 MOHAMMED OWAIS SAYED
#Make sure you run the program from signup.py

from tkinter import *
from tkinter import Tk, StringVar, ttk
import Endpage as s
import tkinter.messagebox

def main():
    root = Tk()
    root.geometry("1360x700+0+0")
    root.title("Train Ticket")  
    root.configure(background='grey')

    Tops = Frame(root, width = 900, height = 700, bd=16, relief ="raise")
    Tops.pack(side=TOP)

    f1 =  Frame(root, width = 1500, height = 650, bd=8, relief="raise")
    f1.pack(side=LEFT)

    fla =  Frame(f1, width = 1600, height = 400, bd=8, relief="raise")
    fla.pack(side=TOP)
    f2a =  Frame(f1, width = 1600, height = 400, bd=6, relief="raise")
    f2a.pack(side=BOTTOM)

    topLeft1 =  Frame(fla, width = 760, height = 400, bd=16, relief="raise")
    topLeft1.pack(side=LEFT)
    topLeft2 =  Frame(fla, width = 800, height = 400, bd=16, relief="raise")
    topLeft2.pack(side=RIGHT)
    topLeft3 =  Frame(fla, width = 500, height = 400, bd=16, relief="raise")
    topLeft3.pack(side=RIGHT)
    #---------------------------------------------------------------------------------------
    bottomLeft1 = Frame(f2a, width = 500, height = 450, bd=14, relief="raise")
    bottomLeft1.pack(side=LEFT)

    bottomLeft2 = Frame(f2a, width = 500, height = 450, bd=14, relief="raise")
    bottomLeft2.pack(side=LEFT)
    #---------------------------------------------------------------------------------------
    Tops.configure(background='black')
    f1.configure(background='black')
    Title = Label(Tops, font=('arial',50,'italic'), text="Train Ticketing System",  height=1,width = 32, bd=6)
    Title.grid(row=0,column=0,pady=15)



    #--Variables
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = StringVar() 

    #---Create Widget topleft1--
    lblclass = Label(topLeft1, font=('arial', 22, 'bold'), text='class', bd=8)
    lblclass.grid(row=0, column=0, sticky=W)
    chkstandard = Checkbutton(topLeft1, font=('arial',20, 'bold'), text='Standard', variable=var1)
    chkstandard.grid(row=1, column=0, sticky=W)
    chkEconomy = Checkbutton(topLeft1, font=('arial',20, 'bold'), text='Economy', variable=var2)
    chkEconomy.grid(row=2, column=0, sticky=W)
    chkFirstClass = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='First Class', variable=var3, onvalue=1, offvalue=0)
    chkFirstClass.grid(row=3, column=0, sticky=W)

    #--Create Widget topLeft2--
    lblselect = Label(topLeft3, font=('arial',20, 'bold'), text='Select A Destination', bd=8)
    lblselect.grid(row=0, column=0, sticky=W, columnspan=2)
    lblDestination = Label(topLeft3, font=('arial',20, 'bold'), text='Destination', bd=8)
    lblDestination.grid(row=1, column=0, sticky=W)

    CboDestination = ttk.Combobox(topLeft3, text = var4, state=' readonly', font=('arial', 22, "bold"), width=22)
    CboDestination['value']=('CST', 'Masjid', 'Sandhurst', 'Dockyard', 'Reay road')
    CboDestination.current(0)
    CboDestination.grid(row=1, column=1)
    chkAdult = Checkbutton(topLeft3, font=('arial',20, 'bold'), text='Adult', variable=var5)
    chkAdult.grid(row=2,column=0, sticky=W)

    chkchild = Checkbutton(topLeft3, font=('arial',20, 'bold'), text='Child', variable=var6)
    chkchild.grid(row=3, column=0, sticky=W)

    lblclass = Label(topLeft2, font=('arial', 22, 'bold'), text='Select Ticket Type', bd=8, width=16)
    lblclass.grid(row=0, column=0, sticky=W)

    chkSingle = Checkbutton(topLeft2, font=('arial',20, 'bold'), text='Single', variable=var7)
    chkSingle.grid(row=1, column=0, sticky=W)
    entSingle = Entry(topLeft2, font=('arial',20, 'bold'), textvariable = var8, bd=2, width=13)
    entSingle.grid(row=1,column=1, sticky=W)
    lblclass = Label(topLeft2, font=('arial', 22, 'bold'), text=' ', bd=8)
    lblclass.grid(row=2, column=0, sticky=W)
    chkReturn = Checkbutton(topLeft2, font=('arial',20, 'bold'), text='Return', variable=var9, onvalue=1, offvalue=0)
    chkReturn.grid(row=3, column=0, sticky=W)
    entReturn = Entry(topLeft2, font=('arial',20, 'bold'), textvariable = var10, bd=2, width=13)
    entReturn.grid(row=3, column=1, sticky=W)

    #--------------------TAX SECTION-----------

    lblstateTax = Label(bottomLeft1, font=('arial', 24, 'bold'), text="State Tax", bd=16, anchor='w', width=25)
    lblstateTax.grid(row=3, column=2)

    txtstateTax = Entry(bottomLeft1, font=('arial', 16, 'bold'), bd=10, width=28, bg="#ffffff", justify="right")
    txtstateTax.grid (row=3, column=3)

    lblSubTotal = Label(bottomLeft1, font=('arial', 24, 'bold'), text="Sub Total", bd=16, anchor='w', width=25)
    lblSubTotal .grid(row=4, column=2)
    txtSubTotal = Entry(bottomLeft1, font=('arial', 16, 'bold'), bd=10, width=28, bg="#ffffff", justify='right')
    txtSubTotal .grid(row=4, column=3)

    lblTotalCost = Label(bottomLeft1, font=('arial', 24, 'bold'), text="Total Cost", bd=16, anchor='w', width=25)
    lblTotalCost.grid(row=5, column=2)
    txtTotalCost = Entry(bottomLeft1, font=('arial', 16, 'bold'), bd=10, width=28, bg="#ffffff", justify='right')
    txtTotalCost.grid(row=5, column=3)

    name = Label(bottomLeft2, font=('arial', 20, 'bold'), text="Enter Name of Buyer", bd=16, anchor='w', width=16)
    name.grid(row=6, column=2)
    name2 = Entry(bottomLeft2, font=('arial', 16, 'bold'), bd=10, width=28, bg="#ffffff", justify='right')
    name2.grid(row=7, column=2)

    Print = Button(bottomLeft2, font=('arial', 20, 'bold'), text="Print", bd=16, anchor='w', width=16, command=s.endpage)
    Print.grid(row=8, column=2)
    
    root.mainloop()