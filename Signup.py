#Make sure you run the program from signup.py

from tkinter import *
import LoginPage as d

root = Tk()
root.geometry('500x500')
root.title("SIGNUP")

label_0 = Label(root,font=('arial',20, 'bold'),text = " Signup ",bg='brown', relief='raise', bd=8, width=20,fg='white')
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name :",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email :",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_1 = Label(root, text="Full Name :",width=20,font=("bold", 10))
label_1.place(x=70,y=230)

entry_1 = Entry(root)
entry_1.place(x=235,y=230)


label_1 = Label(root, text="Password : ",width=20,font=("bold", 10))
label_1.place(x=70,y=280)

entry_1 = Entry(root)
entry_1.place(x=240,y=280)

label_4 = Label(root, text="Confirm Password : ",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(root, text="Male", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root, text="Female", variable=var2).place(x=290,y=330)

Button(root,font=('arial',10, 'bold'),text = "SUBMIT",bg='brown', relief='raise', bd=8, width=20,fg='white', command=d.go).place(x=180,y=380)

root.mainloop()