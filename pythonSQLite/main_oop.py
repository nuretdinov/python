import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO, filename="main.log")

class Db:
    def __init__(self, name):
        self.name = name
        self._conn = self.connection()
        logging.info("Db connection established")

    def creat_db(self):
        connection = sqlite3.connect(f"{self.name}")
        cursor = connection.cursor()
        logging.info("Database created")
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, tel INTEGER);''')
        connection.commit()
        logging.info("Table created")
        cursor.close()

    def connection(self):
        if not os.path.exists(f"{self.name}"):
            self.creat_db()
        return sqlite3.connect(f"{self.name}")

    def _execute_query(self, query, select=False):
        cursor = self._conn.cursor()
        cursor.execute(query)
        if select:
            rows_list = cursor.fetchall()
            cursor.close()
            return rows_list
        else:
            self._conn.commit()
        cursor.close()

    def add_row(self, new_name: str, new_tel: int):
        query = f"""INSERT INTO users (name, tel) VALUES ("{new_name}", "{new_tel}");"""
        self._execute_query(query, select=False)
        logging.info("New record added")

    def select_rows(self):
        query = f"""SELECT * FROM users"""
        rows_list = self._execute_query(query, select=True)
        logging.info("All records sent")
        return rows_list


phonebook = Db('phonebook.db')

# выводим записи
result = phonebook.select_rows()
for field in result:
    print(str(field[0]) + ' ' + str(field[1]) + ' ' + str(field[2]))

# добавляем новую запись
if input('Добавить новую запись (yes/no)?') == 'yes':
    new_name = input('Введите имя новой записи:')
    new_tel = input('Введите телефон новой записи:')
    phonebook.add_row(new_name, new_tel)
    print('Запись добавлена')