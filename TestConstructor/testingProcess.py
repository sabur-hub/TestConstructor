from tkinter import *
from checkingResult import checkingResult
import time


def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def resultFunc(values=None, userValues=None):
    if values is not None:
        with open('result.txt', 'w') as file_w:
            for elem in values:
                file_w.write(elem[2][0] + '\n')
        open('userResult.txt', 'w').close()
    elif userValues is not None:
        with open('userResult.txt', 'a') as file:
            file.write(userValues + '\n')


def testProccess(master, values, login, test_time, amout, counter):
    master.geometry("500x500")
    v = StringVar(master, "1")
    label_0 = Label(master, text=values[counter][0][0] + ") " + values[counter][1][0], width=20, font=("bold", 20))
    label_0.place(x=120, y=53)

    radio1 = Radiobutton(master, text=values[counter][1][1], variable=v,
                         value="A", indicator=0,
                         background="light blue",
                         command=lambda: testController(values, master, login, test_time, amout, v, counter,
                                                        arrElement, time.time()))

    radio2 = Radiobutton(master, text=values[counter][1][2], variable=v,
                         value="B", indicator=0,
                         background="light blue",
                         command=lambda: testController(values, master, login, test_time, amout, v, counter,
                                                        arrElement, time.time()))
    radio3 = Radiobutton(master, text=values[counter][1][3], variable=v,
                         value="C", indicator=0,
                         background="light blue",
                         command=lambda: testController(values, master, login, test_time, amout, v, counter,
                                                        arrElement, time.time()))
    radio1.place(x=100, y=130)
    radio2.place(x=100, y=180)
    radio3.place(x=100, y=230)
    arrElement = [label_0, radio1, radio2, radio3]
    counter += 1


def testController(values, root, login, test_time, amout, v=None, counter=0, arrElement=None, timer=None):
    global start_time
    if v is not None:
        if v.get() == 'A':
            result = 'A'
        elif v.get() == 'B':
            result = 'B'
        else:
            result = 'C'
        resultFunc(None, result)
    elif counter == 0:
        start_time = time.time()
        resultFunc(values)

    if arrElement is not None: destroyElement(arrElement)

    if timer is not None:
        if (test_time - ((timer / 60) - start_time)) < 0:
            checkingResult(root)

    if counter < int(amout):
        testProccess(root, values, login, test_time, amout, counter)
    else:
        checkingResult(root)
