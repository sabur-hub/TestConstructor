from tkinter import *
from tkinter.ttk import *
from testGetter import testGetter


def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def authForm():
    btnRegist = Button(root, text='Registration', command=lambda: authAction(1, [btnRegist, btnLog]))
    btnLog = Button(root, text='Log In', command=lambda: authAction(0, [btnRegist, btnLog]))
    btnRegist.place(x=120, y=100)
    btnLog.place(x=120, y=150)


def takeTestForm():
    label_0 = Label(root, text="Enter config test", width=20, font=("bold", 20))
    label_0.place(x=120, y=53)
    entry_1 = Entry(root, width=30)
    entry_1.place(x=120, y=130)
    btnKey = Button(root, text='Submit',
                    command=lambda: testGetter(root, [label_0, entry_1, btnKey], entry_1.get().strip()))
    btnKey.place(x=120, y=200)


def deleter_one(control):
    destroyElement([btnCreator, btnUser])
    if control:
        authForm()
    elif not control:
        takeTestForm()


def authAction(counter, arr):
    destroyElement(arr)
    from registration import regFunc, LogFunc
    if counter:
        regFunc(root)
    else:
        LogFunc(root)


root = Tk()
root.title('Questioner')
root.geometry('400x350')
style = Style()
style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')

btnCreator = Button(root, text='Create test', command=lambda a=1: deleter_one(a))
btnUser = Button(root, text='Start Quiz', command=lambda a=0: deleter_one(a))
btnCreator.place(x=120, y=100)
btnUser.place(x=120, y=150)

root.mainloop()
