from tkinter import *
import sys
import os


def reload():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def testResult(root, results, right_result, user_result):
    Label(root, text="Correct answer:", width=20, font=("bold", 10)).place(x=66, y=50)
    Label(root, text="Incorrect answer:", width=20, font=("bold", 10)).place(x=200, y=50)
    Label(root, text=str(results[0]), width=20, font=("bold", 10)).place(x=66, y=100)
    Label(root, text=str(results[1]), width=20, font=("bold", 10)).place(x=200, y=100)
    Label(root, text="From 100 your mark is:", width=20, font=("bold", 10)).place(x=60, y=150)
    Label(root, text=str(results[2]), width=20, font=("bold", 10)).place(x=200, y=150)
    Label(root, text="Your answer:", width=20, font=("bold", 10)).place(x=66, y=200)
    Label(root, text="Right answer:", width=20, font=("bold", 10)).place(x=200, y=200)
    y_coordinate = 250
    for elem in range(len(user_result)):
        Label(root, text=user_result[elem], width=20, font=("bold", 10)).place(x=66, y=y_coordinate)
        Label(root, text=right_result[elem], width=20, font=("bold", 10)).place(x=200, y=y_coordinate)
        y_coordinate += 25

    for elem in range(len(user_result), len(right_result)):
        Label(root, text=right_result[elem], width=20, font=("bold", 10)).place(x=136, y=y_coordinate)
        y_coordinate += 25

    btn_reload = Button(root, text='Restart', font=('calibri', 20, 'bold'), borderwidth='4',
                        command=lambda a=1: reload())
    btn_reload.place(x=200, y=400)
