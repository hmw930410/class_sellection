import MySQLdb


def haschoose(username):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        # 查詢該學生所選的課程ID
        cursor.execute("""SELECT course_ID
                          FROM classtable
                          WHERE student_ID = %s
                       """, (username,))
        courseIDs = cursor.fetchall()
        total_credits = 0
        for courseID in courseIDs:
            cursor.execute("""SELECT credits
                              FROM course
                              WHERE course_ID = %s
                           """, (courseID, ))
            credits = cursor.fetchone()[0]
            total_credits += credits
        cursor.execute("""UPDATE student SET total_credit = %s
                          WHERE student_ID = %s
                       """, (total_credits, username))
        db.commit()
        return total_credits

    except Exception as e:
        print("error:", e)
        db.rollback()
        return None
    finally:
        cursor.close()
        db.close()