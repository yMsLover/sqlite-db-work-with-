import dbworker

def main():
    conn = dbworker.DBWorker(r"pySQLite.db")
    print(conn.get_data_from_db())
    conn.close_connection()      

if __name__ == '__main__':
    main()
