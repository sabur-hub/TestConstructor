from testConstructor import testConstructor
from tkinter import messagebox


def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def setConfig(arr, root, arrElement):
    exist = 0
    try:
        with open('key.txt') as file_r:
            for elem in file_r:
                elem = elem.replace('\n', '')
                elem = elem.split('|')
                if elem[0] == arr[0]:
                    exist += 1

        if exist == 0:
            with open('key.txt', 'a') as file:
                if not len(arr[0]) or not len(arr[1]):
                    raise AttributeError
                file.write(arr[0] + '|' + arr[1] + '|' + arr[2] + '|' + arr[3] + '\n')
        else:
            raise AttributeError

        destroyElement(arrElement)
        testConstructor(int(arr[1]), arr[3], root, 1, arr[0])
    except AttributeError:
        messagebox.showerror("error", "Like this config key already exist please enter another one")
