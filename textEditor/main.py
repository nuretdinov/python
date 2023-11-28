from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# глобальная переменная для хранения имени файла, с которым работаем в редакторе
file_name = ''


# функция создания нового файла
def new_file():
    global file_name
    if messagebox.askquestion('Внимание', 'Текущий файл не сохранен \n Все создать новый?') == 'yes':
        main_text_field.delete(1.0, END)
        file_name = ''


# функция открытия файла
def open_file():
    global file_name
    if messagebox.askquestion('Внимание', 'Текущий файл не сохранен \n Все равно открыть?') == 'yes':
        file_name = filedialog.askopenfilename()
        if file_name != "":
            file_name = str(file_name)
            with open(file_name, 'r', encoding="utf8") as f:
                fileText = f.read()
                main_text_field.delete(1.0, END)
                main_text_field.insert(0.0, fileText)


# функция сохранения файла
def save_file():
    global file_name
    if messagebox.askquestion('Сохранение файла', 'Точно сохранить?') == 'yes':
        new_file_text = main_text_field.get(1.0, END)
        if file_name != '':
            with open(file_name, 'w', encoding="utf8") as f:
                f.write(new_file_text)
        else:
            file_name = filedialog.asksaveasfile_name()
            with open(file_name, 'w', encoding="utf8") as f:
                f.write(new_file_text)


# функция выхода из приложения
def exit_app():
    if messagebox.askquestion('Выход из программы', 'Выйти?') == 'yes': window.quit()


# функция изменения цветовой схемы приложения
def theme_white():
    main_text_field['bg'] = 'white'
    main_text_field['fg'] = 'black'


def theme_black():
    main_text_field['bg'] = 'black'
    main_text_field['fg'] = 'white'


# создаем окно приложения
window = Tk()
window.title('Текстовый редактор')
# создаем меню приложения
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=filemenu)
filemenu.add_command(label='Новый', command=new_file)
filemenu.add_command(label='Открыть', command=open_file)
filemenu.add_command(label='Сохранить', command=save_file)
filemenu.add_command(label='Выход', command=exit_app)
theme_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Схема", menu=theme_menu)
theme_menu.add_command(label="Темная", command=theme_black)
theme_menu.add_command(label="Светлая", command=theme_white)
window.config(menu=menubar)
# создаем рабочую область приложения
main_text_field = Text(window, width=90, height=30)
main_text_field.pack(side=LEFT)
scroll = Scrollbar(command=main_text_field.yview)
scroll.pack(side=LEFT, fill=Y)
main_text_field.config(yscrollcommand=scroll.set)
window.mainloop()
