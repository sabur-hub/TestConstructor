from tkinter import *
from authLogicPart import registrationDoc, LogIn


def regFunc(root):
    root.geometry('500x500')
    root.title("Registration Form")
    label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)
    label_2 = Label(root, text="Login", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)
    label_3 = Label(root, text="Password", width=20, font=("bold", 10))
    label_3.place(x=70, y=280)
    entry_3 = Entry(root)
    entry_3.place(x=240, y=280)
    btn = Button(root, text='Submit', width=20, bg='brown', fg='white',
                 command=lambda: registrationDoc([entry_1.get().strip(), entry_2.get().strip(), entry_3.get().strip()]
                                                 , root, [label_0, label_1, label_2, label_3, entry_1, entry_2, entry_3,
                                                          btn]))
    btn.place(x=180, y=380)


def LogFunc(root):
    root.geometry('500x500')
    root.title("LogIn Form")
    label_0 = Label(root, text="LogIn", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, text="LogIn", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)
    label_2 = Label(root, text="Password", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)
    btn = Button(root, text='Submit', width=20, bg='brown', fg='white',
                 command=lambda: LogIn([entry_1.get().strip(), entry_2.get().strip()], root,
                                       [label_0, label_1, label_2, entry_1, entry_2, btn]))
    btn.place(x=180, y=220)
