import sqlite3
from sqlite3 import Error

def connetc_to_db(db_file_path):
    """ Создание соединения с БД SQLite 
    :return: Возвращает объект соединения или None 
    :param db_file_path: файл базы данных
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    
    return conn


def create_table(conn, create_table_sqlite):
    """ Создает таблицу в бд с параметрами create_table_sqlite
    :param conn: объект соединения
    :param create_table_sqlite: инструкция CREATE TABLE
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sqlite)
    except Error as e:
        print(e)

def main():
    db_file_path = r"pytohn_sqlite.db"

    sql_create_project_table =  """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES \
                                    projects (id)
                                );""" 

    conn = connetc_to_db(db_file_path=db_file_path)

    if conn is not None:
        create_table(conn, sql_create_project_table)

        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")                      

if __name__ == '__main__':
    main()
