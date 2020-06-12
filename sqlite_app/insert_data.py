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

def create_project(conn, project):
    sql = '''  INSERT INTO projects(name, begin_date, end_date)
                VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def main():
    db_file_path = r'pytohn_sqlite.db'
    
    conn = connetc_to_db(db_file_path)
    
    with conn:
        project = ('333',
                   '2015-01-01',
                   '2015-01-30')
        project_id = create_project(conn, project)

if __name__ == '__main__':
    main()


     