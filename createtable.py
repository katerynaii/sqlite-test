import sqlite3

connection = sqlite3.connect('phones.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS PHONES")


table = """ CREATE TABLE PHONES (
			phone CHAR(255) NOT NULL,
			id INTEGER PRIMARY KEY,
			name VARCHAR(25)
		); """

cursor.execute(table)

print("Table is Ready")

connection.close()
