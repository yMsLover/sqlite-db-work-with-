import sqlite3
from sqlite3 import Error

class DBWorker:

    def __init__(self, db_file_path):
        """ Подключение к БД """

        self.conn = sqlite3.connect(database=db_file_path)
        self.cur = self.conn.cursor()

    def get_data_from_db(self, status = True):
        """ Получение всех записей в БД.
        :param status: параметр для фильтра записей в конкретном
        случае. Все показывать только где статус True
        """ 
        with self.conn:
            return self.cur.execute("SELECT * FROM users \
                                     WHERE status=?",
                                     (status,)).fetchall()
            #fetchall() формирует список записей на основании SELECT

    def checking_availability(self, user_id):
        """ Проверка есть ли запись в БД """
        with self.conn:
            result = self.cur.execute("SELECT user_id \
                                       FROM users \
                                       WHERE user_id=?",
                                       (user_id,)).fetchall()
        return bool(len(result))
    
    def add_data_to_db(self, user_id, status = True):
        """ Добавление новго пользователя в БД """
        with self.conn:
            return self.cur.execute("INSERT INTO users \
                                     (user_id, status) \
                                      VALUES(?,?)", (user_id, status))

    def update_data_to_db(self, user_id, status):
        """ Обновление данных в БД """
        with self.conn:
            return self.cur.execute("UPDATE users \
                                     SET status = ? \
                                     WHERE user_id = ?", 
                                     (status, user_id))
    
    def close_connection(self):
        """ Закрывает соединение с БД """
        self.cur.close()