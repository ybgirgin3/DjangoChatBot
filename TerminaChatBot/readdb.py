import sqlite3
from sqlite3 import Error

### tablo isimler #####
# kullanıcı isimleri ve şifreleri : register_customuser

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn, tableName):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #£cur.execute("SELECT * FROM tasks")
    cur.execute(f"SELECT * FROM {tableName}")

    rows = cur.fetchall()

    return_list = []
    for row in rows:
        return_list.append(row)
        #print(row)

    return return_list

"""
register_customuser
"""

def main(data):
    #database = r"C:\sqlite\db\pythonsqlite.db"
    database = "../db.sqlite3"
    #database = "db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        ret = select_all_tasks(conn, data)

    return ret


#main()
