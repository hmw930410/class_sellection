import MySQLdb


def deletechoose(username, courseid):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        cursor.execute("""DELETE
                          FROM classtable
                          WHERE course_ID = %s
                       """, (courseid,))
        
        cursor.execute("""SELECT week, begin_time, end_time
                            From course
                            WHERE course_ID = %s
                        """, (courseid,))
        course_info = cursor.fetchone()
        for i in range(course_info[1], course_info[2] + 1):
            table_name = f"student{username}"
            cursor.execute(f"""UPDATE {table_name} SET no{i} = 1
                                WHERE week = {course_info[0]}""")
        cursor.execute("""SELECT now_people
                          From course
                          WHERE course_ID = %s
                        """, (courseid,))
        now_people = cursor.fetchone()[0] - 1
        cursor.execute("""UPDATE course SET now_people = %s
                            WHERE course_ID = %s
                        """, (now_people, courseid, ))

        db.commit()
    except Exception as e:
        print("error:", e)
        db.rollback()
        return None
    finally:
        cursor.close()
        db.close()