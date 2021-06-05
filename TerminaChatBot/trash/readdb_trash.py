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

def insert_to_table(conn, tableName, item_index, item_name, user_index):
    """
    :param: tableName   -> verinin kaydedileceği tablo adı
    :param: user_index  -> işlem yapan kullanıcının indexi (programda ayırt etmek lazım)
    :param: item_name   -> kaydelecek olan elemanın adı

    :param: item index  -> enumeration mantığı ile ana index değeri dönmesi lazım
    
    """
    #değer_gir = #INSERT INTO personel VALUES ('Fırat', 'Özgül', 'Adana')
    cur = conn.cursor()
    cmd = f"INSERT INTO {tableName} VALUES ({item_index}, {item_name}, {user_index})"
    cur.execute(cmd)

    # kayıt işlemi bittikten sonra listeyi komple tekrardan yazdır
    print("işlem başarılı")
    return select_all_tasks(conn, tableName)


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

def main(data,
         fetch = None,
         send = None,
         # eğer send active ise bunlar none olmayacak
         item_index = None,
         item_name = None,
         user_index = None
         ):
    #database = r"C:\sqlite\db\pythonsqlite.db"
    #database = "../db.sqlite3"
    #database = "db.sqlite3"
    database = "../db_trash.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        if fetch:
            return select_all_tasks(conn, data)
        if send:
            return insert_to_table(conn, data, item_index, user_index, item_name)




#main()
