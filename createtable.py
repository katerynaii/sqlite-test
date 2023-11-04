def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Phones (
        phoneID INTEGER PRIMARY KEY,
        phoneValue varchar(255),
        contactName varchar(255)
        );
        """
    cur.execute(sql)

    con.commit()
    con.close()
