from tkinter import *
from tkinter import messagebox


def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def testConstructor(amount, login, root, counter, key):
    if counter <= amount:
        root.geometry('500x500')
        root.title(f'Welcome to program {login} ')
        label_0 = Label(root, text=f"Add {counter} Question {login}", width=20, font=("bold", 20))
        label_0.place(x=90, y=53)
        entry_0 = Entry(root)
        entry_0.place(x=180, y=130, width=250, height=30)
        label_1 = Label(root, text="A", width=20, font=("bold", 10))
        label_1.place(x=66, y=180)
        entry_1 = Entry(root)
        entry_1.place(x=200, y=180)
        label_2 = Label(root, text="B", width=20, font=("bold", 10))
        label_2.place(x=68, y=230)
        entry_2 = Entry(root)
        entry_2.place(x=200, y=230)
        label_3 = Label(root, text="C", width=20, font=("bold", 10))
        label_3.place(x=70, y=280)
        entry_3 = Entry(root)
        entry_3.place(x=200, y=280)
        label_4 = Label(root, text="Right Answer", width=20, font=("bold", 10))
        label_4.place(x=70, y=330)
        entry_4 = Entry(root)
        entry_4.place(x=200, y=330)
        counter += 1
        btn = Button(root, text='Submit', width=20, bg='brown', fg='white',command=lambda: controler(amount, login,
            root, counter, key, [entry_0.get(), entry_1.get(), entry_2.get(), entry_3.get()], entry_4.get(), [label_0,
            label_1, label_2, label_3, label_4, entry_0, entry_1, entry_2, entry_3, entry_4, btn]))
        btn.place(x=180, y=380)
    else:
        messagebox.showinfo("End of test", f"You inputted all test please give this key = {key} to the person who "
                                           f"gonna take this tes")


def controler(amount, login, root, counter, key, arr, answer, arrElement):
    with open(f'{key}.txt', 'a') as file:
        file.write('Amount ' + str(counter - 1) + '\n')
        for elem in arr:
            file.write(elem + '\n')
        else:
            file.write('Answer: ' + answer + '\n')
    destroyElement(arrElement)
    testConstructor(amount, login, root, counter, key)
