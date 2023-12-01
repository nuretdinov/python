import sqlite3
from tkinter import messagebox
from tkinter import *

root = Tk()

# соединение с БД
with sqlite3.connect('phonebook.db') as conn:
    cursor = conn.cursor()

# используем для обновления вывода списка контактов
var_change_contact_list = StringVar()

# функция вывода содержимого записной книжки
def get_phonebook():
    bd_content = ''
    cursor.execute('SELECT * FROM users')
    fields = cursor.fetchall()
    for field in fields:
        bd_content = bd_content + str(field[0]) + ' ' + str(field[1]) + ' ' + str(field[2]) + '\n'
    var_change_contact_list.set(bd_content)

get_phonebook()

# функция добавления нового контакта
def add_contact():
    new_name = ent_new_name.get()
    new_tel = ent_new_tel.get()
    if new_name != '' and new_tel != '':
        try:
            cursor.execute('INSERT INTO users (name, tel) VALUES (?, ?)', (new_name, new_tel))
        except sqlite3.DatabaseError as err:
            messagebox.showerror('Ошибка', err)
        else:
            conn.commit()
        get_phonebook()
        ent_new_name.delete(0, END)
        ent_new_tel.delete(0, END)
        messagebox.showinfo('', 'Запись добавлена!')
        get_phonebook()
    else:
        messagebox.showerror('Запись не добавлена', 'Заполните поля!')

root.title('Записная книжка')
# формируем область для вывода записной книжки
db_content_group = LabelFrame(root, text='Содержимое записной книжки', padx=20, pady=20)
db_content_label = Label(db_content_group, textvariable=var_change_contact_list, justify=LEFT)
db_content_label.pack()
db_content_group.pack(pady=10, padx=10)

# формируем поля для добавления записей
db_add_group = LabelFrame(root, text='Добавить новую запись', padx=20, pady=20)
Label(db_add_group, text='Имя нового контакта').pack()
ent_new_name = Entry(db_add_group)
ent_new_name.pack(pady=5, padx=5)
Label(db_add_group, text='Телефон нового контакта').pack()
ent_new_tel = Entry(db_add_group)
ent_new_tel.pack(pady=5, padx=5)
Button(db_add_group, text=' Добавить ', command=add_contact).pack(pady=5, padx=5)
db_add_group.pack(pady=10, padx=10)

root.mainloop()
