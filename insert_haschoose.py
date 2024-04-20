import MySQLdb


def haschoose(table, username):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        for row in table:
            course_ID = row[0]
            # 檢查課程是否被該學生選過
            cursor.execute("""SELECT COUNT(*)
                              FROM classtable
                              WHERE student_ID = %s AND course_ID = %s
                           """, (username, course_ID))
            result = cursor.fetchone()
            if result[0] == 0:
                cursor.execute("""INSERT INTO classtable (student_ID,
                                  course_ID) VALUES (%s, %s)
                               """, (username, row[0]))

        db.commit()

        return table
    except Exception as e:
        print("error:", e)
        db.rollback()
        return None
    finally:
        cursor.close()
        db.close()