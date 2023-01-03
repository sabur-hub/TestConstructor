from testingProcess import testController
from tkinter import messagebox

def destroyElement(arr):
    for elem in arr:
        elem.destroy()


def testGetter(root, arrElement, key):
    config = []
    dataTest = []
    try:
        with open('key.txt') as file:
            for elem in file:
                elem = elem.replace('\n', '')
                elem = elem.strip().split('|')
                if elem[0] == key:
                    config = [elem[0], elem[1], elem[2], elem[3]]

        if not len(config):
            raise ValueError
    except ValueError:
        messagebox.showerror("error", "Test with this config test not founded")

    with open(f'{key}.txt', 'r') as file:
        counter = 0
        for elem in file:
            elem.replace('\n', '')
            elem.strip()
            if 'Amount' in elem:
                dataTest.append([[], [], []])
                dataTest[counter][0].append(elem.replace('Amount', '').strip())
            elif 'Answer' in elem:
                elem = elem.replace('Answer:', '').strip()
                dataTest[counter][2].append(elem)
                counter += 1
            else:
                dataTest[counter][1].append(elem)

    destroyElement(arrElement)
    testController(dataTest, root, config[3], int(config[2]), config[1])
