from flask import session
import MySQLdb


def Action(username, password):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()

        cursor.execute("""SELECT *
                          FROM student
                          WHERE student_ID = %s AND PASSWORD = %s
                          """, (username, password,))
        account = cursor.fetchone()
        print(account)
        if account:
            session['success'] = True
            session['username'] = account['id']
            return True

    except Exception as e:
        print("Error:", e)
        return False