import MySQLdb


def canchoose(username):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()

        cursor.execute("""
            SELECT course_ID, course_name, credits, need, open_class,
                class_time, classroom, teacher, Max_people, now_people
            FROM course
            WHERE course_ID NOT IN (
                SELECT classtable.course_ID
                FROM classtable
                WHERE classtable.student_ID = %s)
            AND department_ID = (SELECT department_ID FROM student WHERE student_ID = %s)
            AND course_name NOT IN (
                SELECT course_name
                FROM classtable
                JOIN course ON classtable.course_ID = course.course_ID
                WHERE classtable.student_ID = %s
            );""", (username, username, username))
        tables = cursor.fetchall()
        return tables
    except Exception as e:
        print("Error:", e)
        return None
