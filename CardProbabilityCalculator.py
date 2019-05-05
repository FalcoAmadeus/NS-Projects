import operator as op
from functools import reduce
import tkinter as tk
from functools import partial
import math


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def call_result(
        label_result,
        x,
        y,
        z,
        w,
):
    x = x.get()
    y = y.get()
    z = z.get()
    w = w.get()
    first = ncr(y, w) * ncr(x - y, z - w) / ncr(x, z)
    list = [first]
    play = True
    while play == True:
        if y > 1:
            global perc
            perc = sum(list)
            w = w + 1
            second = ncr(y, w) * ncr(x - y, z - w) / ncr(x, z)
            list.insert(0, second)

        if w == y:
            play = False

        if w and y == 1:
            perc = first
            play = False
        else:
            if w >= y:
                play = False

    label_result.config(text=round_up(perc * 100))
    return


root = tk.Tk()
root.geometry('300x175+100+200')
root.title('Card Probability Calculator')

number1 = tk.IntVar()
number2 = tk.IntVar()
number3 = tk.IntVar()
number4 = tk.IntVar()

labelTitle = tk.Label(root, text='Card Game Probability Calculator').grid(row=0, column=2)
labelx = tk.Label(root, text='Deck Size').grid(row=1, column=1)
labely = tk.Label(root, text='Card Copies').grid(row=2, column=1)
labelz = tk.Label(root, text='Hand Size').grid(row=3, column=1)
labelw = tk.Label(root, text='Copies in hand').grid(row=4, column=1)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2, )

x = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
y = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
z = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
w = tk.Entry(root, textvariable=number4).grid(row=4, column=2)

call_result = partial(
    call_result,
    labelResult,
    number1,
    number2,
    number3,
    number4,
)
buttonCal = tk.Button(root, text='Calculate Percentage', command=call_result).grid(row=5, column=2)
root.mainloop()



