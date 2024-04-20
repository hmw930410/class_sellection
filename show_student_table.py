import MySQLdb


def student_table(username):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        cursor.execute("""
            SELECT course.course_ID, course.course_name, course.need, 
                   course.class_time, course.teacher, course.classroom
            FROM classtable
            JOIN course ON classtable.course_ID = course.course_ID
            WHERE classtable.student_ID = %s""", (username,))
        table = cursor.fetchall()
        return table
    except Exception as e:
        print("Error:", e)
        return None
