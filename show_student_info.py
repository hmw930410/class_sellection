import MySQLdb


def student_info(username):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()

        cursor.execute("""
            SELECT student.student_ID, student.student_name, class_list.classname, student.total_credit
            FROM student
            JOIN class_list ON student.class_ID = class_list.class_ID
            WHERE student.student_ID = %s
        """, (username,))
        students = cursor.fetchall()
        return students
    except Exception as e:
        print("Error:", e)
        return None
