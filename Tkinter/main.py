from tkinter import *
from tkinter import messagebox

window = Tk()

#функция выхода из проиложения
def exitApp():
    if messagebox.askquestion('Выход из программы', 'Выйти?') == 'yes': window.quit()

#формируем окно приложения
window.title('Анкетирование')
window.geometry('400x400+100+50')
menubar = Menu(window)

#формируем меню приложения
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=filemenu)
filemenu.add_command(label='Новый')
filemenu.add_command(label='Открыть')
filemenu.add_command(label='Выход', command=exitApp)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Правка", menu=editmenu)
editmenu.add_command(label="Вырезать")
editmenu.add_command(label="Копировать")
editmenu.add_command(label="Вставить")

window.config(menu=menubar)

# from tkinter import messagebox
# messagebox.showinfo('Message Title', 'Message')
# messagebox.showerror('Message Title', 'Message')
# messagebox.showwarning('Message Title', 'Message')
# messagebox.askquestion('Message Title', 'Message') # yes/no

#функция обработки данных из полей
def getData():

    #создали список для хранения полученных данных
    userData = {'name': '', 'subscrType': '', 'agree1': '', 'agree2': '', 'email': ''}

    #получили и сохранили имя
    userName = userNameEntry.get()
    userData['name'] = userName

    #получили и сохранили список подписок
    selectedProduct = listProducts.curselection()
    nameSelectedProduct = listProducts.get(selectedProduct)
    #print(selectedProduct)
    userData['subscrType'] = nameSelectedProduct

    #проверили чекбоксы и сохранили данные
    if boxAgree1Checked.get() == 1:
        userData['agree1'] = 'На обработку данных согласен'
    if boxAgree2Checked.get() == 1:
        userData['agree2'] = 'На подписку согласен'

    #получили данные из поля с адресом электронной почты
    userEmail = userEmailEntry.get()
    userData['email'] = userEmail

    #сформировали результирующие данные
    result = userData['name'] + '\n' + userData['subscrType'] + '\n' + userData['agree1'] + '\n' + userData['agree2'] + '\n' + userData['email']

    messagebox.showinfo('Ваши данные', result)

#формируем поля анкеты
Label(window, text='Заполните данные анкеты', font='Arial 12').pack()

#текстовое поле ввода
Label(window, text='Введите имя').pack()
userNameEntry = Entry(window)
userNameEntry.pack(pady=10)

#список
Label(window, text='Выберите продукт').pack()
listProducts = Listbox(window, height=3)
listProducts.insert(1, 'Интернет')
listProducts.insert(2, 'ТВ')
listProducts.insert(3, 'Интернет+ТВ')
listProducts.pack(padx=0, pady=10)

#чекбокс
boxAgree1Checked = IntVar()
boxAgree2Checked = IntVar()
boxAgree1 = Checkbutton(window, text='Согласие на обраотку данных', variable=boxAgree1Checked, onvalue=1)
boxAgree2 = Checkbutton(window, text='Согласие на подписку', variable=boxAgree2Checked, onvalue=1)
boxAgree1.pack()
boxAgree2.pack()

#группировка
group1 = LabelFrame(window, text='Идентификатор пользователя', padx=5, pady=5)
textLabel = Label(group1, text='E-mail: ')
userEmailEntry = Entry(group1)
group1.pack(pady=10, padx=10)
textLabel.pack(side=LEFT)
userEmailEntry.pack(side=RIGHT)

#кнопка подписку
Button(window, text=' Оформить подписку ', command=getData).pack()

window.mainloop()