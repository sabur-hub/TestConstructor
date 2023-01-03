from configTest import configTest
from tkinter import messagebox


def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def registrationDoc(arr, root, arrElement):
    exist = 0
    try:
        with open('user.txt') as file_r:
            for elem in file_r:
                elem = elem.replace('\n', '')
                elem = elem.split('|')
                if elem[1] in arr: exist += 1

        if exist == 0:
            with open('user.txt', 'a') as file:
                for elem in arr:
                    if not len(elem):
                        raise UserWarning
                    file.write(elem + '|')
                else:
                    file.write('\n')
        else:
            raise UserWarning

        destroyElement(arrElement)
        configTest(root, arr[1])
    except UserWarning:
        messagebox.showerror("error", "Registration error you inputted wrong data or like this user already exist")


def LogIn(arr, root, arrElement):
    exist = 0
    try:
        with open('user.txt') as file_r:
            for elem in file_r:
                elem = elem.replace('\n', '')
                elem = elem.split('|')
                if elem[1] in arr and elem[2] in arr: exist += 1

        if (not exist):
            raise UserWarning

        destroyElement(arrElement)
        configTest(root, arr[0])
    except:
        messagebox.showerror("error", "Log In error like this user not founded")
