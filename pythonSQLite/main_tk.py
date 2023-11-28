import sqlite3
from tkinter import messagebox
from tkinter import *

root = Tk()

#соединение с БД
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

#используем для обновления вывода списка контактов
varChangeContactList = StringVar()

#функция вывода содержимого записной книжки
def getPhonebook():
    bdContent = ''
    cursor.execute('SELECT * FROM users')
    fields = cursor.fetchall()
    for field in fields:
        bdContent = bdContent + str(field[0]) + ' ' + str(field[1]) + ' ' + str(field[2]) + '\n'
    varChangeContactList.set(bdContent)
getPhonebook()

#функция добавления нового контакта
def addContact():
    newName = ent_newName.get()
    newTel = ent_newTel.get()
    if newName != '' and newTel != '':
        cursor.execute('INSERT INTO users (name, tel) VALUES (?, ?)', (newName, newTel))
        conn.commit()
        getPhonebook()
        ent_newName.delete(0, END)
        ent_newTel.delete(0, END)
        messagebox.showinfo('', 'Запись добавлена!')
        getPhonebook()
    else:
        messagebox.showerror('Запись не добавлена', 'Заполните поля!')


root.title('Записная книжка')
#формируем область для вывода записной книжки
dbContentGroup = LabelFrame(root, text='Содержимое записной книжки', padx=20, pady=20)
dbContentLabel = Label(dbContentGroup, textvariable=varChangeContactList, justify=LEFT)
dbContentLabel.pack()
dbContentGroup.pack(pady=10, padx=10)

#формируем поля для добавления записей
dbAddGroup = LabelFrame(root, text='Добавить новую запись', padx=20, pady=20)
Label(dbAddGroup, text='Имя нового контакта').pack()
ent_newName = Entry(dbAddGroup)
ent_newName.pack(pady=5, padx=5)
Label(dbAddGroup, text='Телефон нового контакта').pack()
ent_newTel = Entry(dbAddGroup)
ent_newTel.pack(pady=5, padx=5)
Button(dbAddGroup, text=' Добавить ', command=addContact).pack(pady=5, padx=5)
dbAddGroup.pack(pady=10, padx=10)

root.mainloop()