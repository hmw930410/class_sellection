import MySQLdb
from flask import request


def userLogin():
    
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                     user="test",
                     passwd="123",
                     db="show_sql")
        cursor = db.cursor()
        
        username = request.form['username']
        password = request.form['password']
        
        # 查詢數據庫
        cursor.execute("""
                    SELECT *
                    FROM student
                    WHERE student_ID = %s
                    AND PASSWORD = %s
                    """, (username, password))
        user = cursor.fetchone()
        print("User: ", user)
        
    except Exception as e:
        print("Error:", e)
        return None