def create_table():
    import sqlite3

    connection = sqlite3.connect('phones.db')

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS PHONES")


    table = """ CREATE TABLE PHONES (
                phoneValue CHAR(255) NOT NULL,
                phoneID INTEGER PRIMARY KEY,
                contactName VARCHAR(25)
            ); """

    cursor.execute(table)

    print("Table is Ready")

    connection.close()
