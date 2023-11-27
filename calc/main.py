def calc():
    num1 = EntryA.get()
    num2 = EntryB.get()
    mathSing = EntryC.get()

    if num1 != '' and num2 != '' and mathSing != '':
        try:
            num1 = float(num1)
            num2 = float(num2)
            match mathSing:
                case "+": result = round(num1 + num2)
                case "-": result = round(num1 - num2)
                case "*": result = round(num1 * num2)
                case "/":
                    if num2 != 0: result = round(num1 / num2, 2)
                    else: result = 'Ошибка, 0!'
                case _: result = 'Ошибка, знак!'
        except ValueError: result = 'Ошибка, числа!'
    else:
        result = 'Ошибка, поля!'

    Result.delete(0, END)
    Result.insert(0, result)

from tkinter import *

root = Tk()
root.geometry('300x300+200+200')
root.title('Калькулятор')
Label(root, text='Первое число', font='Arial 12', height=2).pack()
EntryA = Entry(root, width=10, font='Arial 12')
EntryA.pack()
Label(root, text='Второе число', font='Arial 12', height=2).pack()
EntryB = Entry(root, width=10, font='Arial 12')
EntryB.pack()
Label(root, text='Знак действия', font='Arial 12', height=2).pack()
EntryC = Entry(root, width=10, font='Arial 12')
EntryC.pack()
Button(root, text='     =     ', font='Arial 12', command=calc).pack()
Label(root, text='Результат', font='Arial 12', height=2).pack()
Result = Entry(root, width=14, font='Arial 12')
Result.pack()
root.mainloop()