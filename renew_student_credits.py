import MySQLdb


def haschoose(table, username):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        for row in table:
            cursor.execute("""INSERT INTO classtable (student_ID, course_ID) 
                           VALUES (%s, %s)""", (username, row[0]))

        # 提交事務
        db.commit()

        return table
    except Exception as e:
        print("error:", e)
        db.rollback()
        return None
    finally:
        cursor.close()
        db.close()