from tkinter import *
from tkinter import messagebox

# функция обработки данных из полей
def get_data():
    # создали список для хранения полученных данных
    user_data = {'name': '', 'subscrType': '', 'agree1': '', 'agree2': '', 'email': ''}
    # получили и сохранили имя
    user_name = ent_user_name.get()
    user_data['name'] = user_name
    # получили и сохранили список подписок
    selected_product = list_products.curselection()
    name_selected_product = list_products.get(selected_product)
    user_data['subscrType'] = name_selected_product
    # проверили чекбоксы и сохранили данные
    if box_agree1_checked.get() == 1:
        user_data['agree1'] = 'На обработку данных согласен'
    if box_agree2_checked.get() == 1:
        user_data['agree2'] = 'На подписку согласен'
    # получили данные из поля с адресом электронной почты
    userEmail = ent_user_email.get()
    user_data['email'] = userEmail
    # сформировали результирующие данные
    result = user_data['name'] + '\n' + user_data['subscrType'] + '\n' + user_data['agree1'] + '\n' + user_data[
        'agree2'] + '\n' + user_data['email']
    messagebox.showinfo('Ваши данные', result)

# функция выхода из проиложения
def exit_app():
    if messagebox.askquestion('Выход из программы', 'Выйти?') == 'yes':
        window.quit()

window = Tk()
# формируем окно приложения
window.title('Анкетирование')
window.geometry('400x400+100+50')
menubar = Menu(window)
# формируем меню приложения
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=filemenu)
filemenu.add_command(label='Новый')
filemenu.add_command(label='Открыть')
filemenu.add_command(label='Выход', command=exit_app)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Правка", menu=editmenu)
editmenu.add_command(label="Вырезать")
editmenu.add_command(label="Копировать")
editmenu.add_command(label="Вставить")
window.config(menu=menubar)

# формируем поля анкеты
Label(window, text='Заполните данные анкеты', font='Arial 12').pack()
# текстовое поле ввода
Label(window, text='Введите имя').pack()
ent_user_name = Entry(window)
ent_user_name.pack(pady=10)
# список
Label(window, text='Выберите продукт').pack()
list_products = Listbox(window, height=3)
list_products.insert(1, 'Интернет')
list_products.insert(2, 'ТВ')
list_products.insert(3, 'Интернет+ТВ')
list_products.pack(padx=0, pady=10)
# чекбокс
box_agree1_checked = IntVar()
box_agree2_checked = IntVar()
chk_box_agree1 = Checkbutton(window, text='Согласие на обраотку данных', variable=box_agree1_checked, onvalue=1)
chk_box_agree2 = Checkbutton(window, text='Согласие на подписку', variable=box_agree2_checked, onvalue=1)
chk_box_agree1.pack()
chk_box_agree2.pack()
# группировка
group1 = LabelFrame(window, text='Идентификатор пользователя', padx=5, pady=5)
txt_label = Label(group1, text='E-mail: ')
ent_user_email = Entry(group1)
group1.pack(pady=10, padx=10)
txt_label.pack(side=LEFT)
ent_user_email.pack(side=RIGHT)
# кнопка подписку
Button(window, text=' Оформить подписку ', command=get_data).pack()

window.mainloop()
