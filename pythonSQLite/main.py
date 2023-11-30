import sqlite3

connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

"""
# Создаем БД
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, tel INTEGER);''') #NULL REAL BLOB
cursor.execute('''ALTER TABLE users ADD COLUMN surname TEXT''')
conn.close()
"""


def get_phonebook():
    # выводим структуру таблицы
    cursor.execute("PRAGMA table_info(users)")
    fields = cursor.fetchall()
    fields_name = ''
    for field in fields:
        fields_name = fields_name + field[1] + ' '
    print(fields_name)
    # выводим содержимое таблицы
    cursor.execute('SELECT * FROM users')
    fields = cursor.fetchall()
    for field in fields:
        print(str(field[0]) + ' ' + str(field[1]) + ' ' + str(field[2]))


# запускаем функцию вывода содержимого
get_phonebook()

# добавляем новую запись
if input('Добавить новую запись (yes/no)?') == 'yes':
    new_name = input('Введите имя новой записи:')
    new_tel = input('Введите телефон новой записи:')
    cursor.execute('INSERT INTO users (name, tel) VALUES (?, ?)', (new_name, new_tel))
    connection.commit()
    get_phonebook()
    print('Запись добавлена')

connection.close()
