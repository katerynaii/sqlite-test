def commit_sql(sql: str):
    import sqlite3

    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()


