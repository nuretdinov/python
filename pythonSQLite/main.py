import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

"""
#Создаем БД
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, tel INTEGER)''') #NULL REAL BLOB
#cursor.execute('''ALTER TABLE users ADD COLUMN surname TEXT''')
conn.close()
"""

def getPhonebook():
    # выводим структуру таблицы
    cursor.execute("PRAGMA table_info(users)")
    fields = cursor.fetchall()
    fieldsName = ''
    for field in fields:
        fieldsName = fieldsName + field[1] + ' '
    print(fieldsName)
    # выводим содержимое таблицыё
    cursor.execute('SELECT * FROM users')
    fields = cursor.fetchall()
    for field in fields:
        print(str(field[0]) + ' ' + str(field[1]) + ' ' + str(field[2]))

#запускаем функцию
getPhonebook()

#добавляем новую запись
if input('Добавить новую запись (да/нет)?') == 'да':
    newName = input('Введите имя новой записи:')
    newTel = input('Введите телефон новой записи:')
    cursor.execute('INSERT INTO users (name, tel) VALUES (?, ?)', (newName, newTel))
    conn.commit()
    getPhonebook()
    print('Запись добавлена')

conn.close()

