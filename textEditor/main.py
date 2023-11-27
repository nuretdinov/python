from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#глобальная переменная для хранения имени файла, с которым работаем в редакторе
fileName = ''

#функция создания нового файла
def newFile():
    global fileName
    if messagebox.askquestion('Внимание', 'Текущий файл не сохранен \n Все создать новый?') == 'yes':
        mainTextField.delete(1.0, END)
        fileName = ''

#функция открытия файла
def openFile():
    global fileName
    if messagebox.askquestion('Внимание', 'Текущий файл не сохранен \n Все равно открыть?') == 'yes':
        fileName = filedialog.askopenfilename()
        if fileName != "":
            fileName = str(fileName)
            with open(fileName, 'r', encoding="utf8") as f:
                fileText = f.read()
                mainTextField.delete(1.0, END)
                mainTextField.insert(0.0, fileText)

#функция сохранения файла
def saveFile():
    global fileName
    if messagebox.askquestion('Сохранение файла', 'Точно сохранить?') == 'yes':
        newFileText = mainTextField.get(1.0, END)
        if fileName != '':
            with open(fileName, 'w', encoding="utf8") as f:
                f.write(newFileText)
        else:
            fileName = filedialog.asksaveasfilename()
            with open(fileName, 'w', encoding="utf8") as f:
                f.write(newFileText)

#функция выхода из приложения
def exitApp():
    if messagebox.askquestion('Выход из программы', 'Выйти?') == 'yes': window.quit()

#функция изменения цветовой схемы приложения
def themeWhite():
    mainTextField['bg'] = 'white'
    mainTextField['fg'] = 'black'

def themeBlack():
    mainTextField['bg'] = 'black'
    mainTextField['fg'] = 'white'

#создаем окно приложения
window = Tk()
window.title('Текстовый редактор')
#создаем меню приложения
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Файл', menu=filemenu)
filemenu.add_command(label='Новый', command=newFile)
filemenu.add_command(label='Открыть', command=openFile)
filemenu.add_command(label='Сохранить', command=saveFile)
filemenu.add_command(label='Выход', command=exitApp)
themMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Схема", menu=themMenu)
themMenu.add_command(label="Темная", command=themeBlack)
themMenu.add_command(label="Светлая", command=themeWhite)
window.config(menu=menubar)
#создаем рабочую область приложения
mainTextField = Text(window, width=90, height=30)
mainTextField.pack(side=LEFT)
scroll = Scrollbar(command=mainTextField.yview)
scroll.pack(side=LEFT, fill=Y)
mainTextField.config(yscrollcommand=scroll.set)
window.mainloop()