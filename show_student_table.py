import MySQLdb


def student_table(username):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()

        cursor.execute("SELECT class_ID FROM student WHERE student_ID = %s", (username,))
        class_ID = cursor.fetchone()[0] 
        print("class", class_ID)
        cursor.execute("""
            SELECT course.course_ID, course.course_name, course.class_time, course.teacher, course.classroom
            FROM course
            WHERE course.need = "yes"
            AND open_class = (SELECT classname FROM class_list WHERE class_ID = %s)
        """, (class_ID,))
        table = cursor.fetchall()
        print(table)
        return table
    except Exception as e:
        print("Error:", e)
        return None

    