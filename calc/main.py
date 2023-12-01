from tkinter import *

def calc():
    num1 = ent_num1.get()
    num2 = ent_num2.get()
    math_sing = ent_math_sign.get()

    if num1 != '' and num2 != '' and math_sing != '':
        try:
            num1 = float(num1)
            num2 = float(num2)
            match math_sing:
                case "+":
                    result = round(num1 + num2)
                case "-":
                    result = round(num1 - num2)
                case "*":
                    result = round(num1 * num2)
                case "/":
                    if num2 != 0:
                        result = round(num1 / num2, 2)
                    else:
                        result = 'Ошибка, 0!'
                case _:
                    result = 'Ошибка, знак!'
        except ValueError:
            result = 'Ошибка, числа!'
    else:
        result = 'Ошибка, поля!'

    ent_result.delete(0, END)
    ent_result.insert(0, result)

root = Tk()
root.geometry('300x300+200+200')
root.title('Калькулятор')
Label(root, text='Первое число', font='Arial 12', height=2).pack()
ent_num1 = Entry(root, width=10, font='Arial 12')
ent_num1.pack()
Label(root, text='Второе число', font='Arial 12', height=2).pack()
ent_num2 = Entry(root, width=10, font='Arial 12')
ent_num2.pack()
Label(root, text='Знак действия', font='Arial 12', height=2).pack()
ent_math_sign = Entry(root, width=10, font='Arial 12')
ent_math_sign.pack()
Button(root, text='     =     ', font='Arial 12', command=calc).pack()
Label(root, text='Результат', font='Arial 12', height=2).pack()
ent_result = Entry(root, width=14, font='Arial 12')
ent_result.pack()
root.mainloop()
