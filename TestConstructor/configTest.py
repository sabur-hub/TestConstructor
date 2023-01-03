from tkinter import *
from testLogic import setConfig

def configTest(root, login):
    root.geometry('500x500')
    root.title("Test config")
    label_0 = Label(root, text="Test config", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, text="Config key", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)
    label_2 = Label(root, text="Amount of test", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)
    label_3 = Label(root, text="time", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    entry_3 = Entry(root)
    entry_3.place(x=240, y=230)
    btn = Button(root, text='Submit', width=20, bg='brown', fg='white',
           command=lambda: setConfig([entry_1.get().strip(), entry_2.get().strip(), entry_3.get().strip(), login],root,
                                     [label_0, label_1, label_2, label_3, entry_1, entry_2, entry_3, btn]))
    btn.place(x=180, y=280)

