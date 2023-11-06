from flask import Flask, request
from utils import commit_sql
from createtable import create_table

app = Flask(__name__)
create_table()


@app.route('/phone/create')
def phones_create():
    phone_value = request.args.get('Phone', '111')

    sql = f"""
    INSERT INTO Phones (phoneValue)
    VALUES ({phone_value});
    """
    commit_sql(sql)

    return 'phones_create'


@app.route('/phone/read')
def phones_read():
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


@app.route('/phone/update')
def phones_update():
    phone_value = request.args['phone']
    phone_id = request.args['id']

    sql = f"""
    UPDATE Phones
    SET phoneValue = '{phone_value}'
    WHERE phoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_update'


@app.route('/phone/delete')
def phones_delete():
    phone_id = request.args['id']

    sql = f"""
    DELETE FROM Phones
    WHERE phoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

