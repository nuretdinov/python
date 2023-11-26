num1 = 0
num2 = 0
mathSing = ''

def num(x):
    EntryCalc.insert(END, x)

def sign(z):
    global num1
    global mathSing
    num1 = EntryCalc.get()
    EntryCalc.delete(0, END)
    mathSing = z

def clr():
    EntryCalc.delete(0, END)

def equal():
    global num1
    global num2
    global mathSing
    num2 = EntryCalc.get()
    EntryCalc.delete(0, END)
    num1 = int(num1)
    num2 = int(num2)
    match mathSing:
        case "+": result = num1 + num2
        case "-": result = num1 - num2
        case "*": result = num1 * num2
        case "/":
            try: result = round(num1 / num2, 2)
            except ZeroDivisionError: result = 'Ошибка, 0!'
        case _:
            result = 'Ошибка, знак!'
    EntryCalc.delete(0, END)
    EntryCalc.insert(0, result)

from tkinter import *
root = Tk()
root.geometry('170x210+200+200')
root.title('Калькулятор')
EntryCalc = Entry(root, width=14, font='Arial 12')
EntryCalc.grid(row=1, column=1, columnspan=4, pady=5, padx=5)
Button(root, text=' 7 ', font='Arial 12', command=lambda: num(7)).grid(row=2, column=1, pady=5, padx=5)
Button(root, text=' 8 ', font='Arial 12', command=lambda: num(8)).grid(row=2, column=2, pady=5, padx=5)
Button(root, text=' 9 ', font='Arial 12', command=lambda: num(9)).grid(row=2, column=3, pady=5, padx=5)
Button(root, text=' 4 ', font='Arial 12', command=lambda: num(4)).grid(row=3, column=1, pady=5, padx=5)
Button(root, text=' 5 ', font='Arial 12', command=lambda: num(5)).grid(row=3, column=2, pady=5, padx=5)
Button(root, text=' 6 ', font='Arial 12', command=lambda: num(6)).grid(row=3, column=3, pady=5, padx=5)
Button(root, text=' 1 ', font='Arial 12', command=lambda: num(1)).grid(row=4, column=1, pady=5, padx=5)
Button(root, text=' 2 ', font='Arial 12', command=lambda: num(2)).grid(row=4, column=2, pady=5, padx=5)
Button(root, text=' 3 ', font='Arial 12', command=lambda: num(3)).grid(row=4, column=3, pady=5, padx=5)
Button(root, text=' 0 ', font='Arial 12', command=lambda: num(0)).grid(row=5, column=2, pady=5, padx=5)
Button(root, text=' / ', font='Arial 12', command=lambda: sign('/')).grid(row=2, column=4, pady=5, padx=5)
Button(root, text=' * ', font='Arial 12', command=lambda: sign('*')).grid(row=3, column=4, pady=5, padx=5)
Button(root, text=' - ', font='Arial 12', command=lambda: sign('-')).grid(row=4, column=4, pady=5, padx=5)
Button(root, text=' + ', font='Arial 12', command=lambda: sign('+')).grid(row=5, column=4, pady=5, padx=5)
Button(root, text=' c ', font='Arial 12', command=clr).grid(row=5, column=1, pady=5, padx=5)
Button(root, text=' = ', font='Arial 12', command=equal).grid(row=5, column=3, pady=5, padx=5)
root.mainloop()