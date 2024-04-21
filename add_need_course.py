import MySQLdb
import renew_student_credits
import insert_haschoose


def addcourse(username):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()

        cursor.execute("SELECT class_ID FROM student WHERE student_ID = %s",
                       (username,))
        class_ID = cursor.fetchone()[0]
        cursor.execute("""
            SELECT course.course_ID, course.course_name, course.need,
                   course.class_time, course.teacher, course.classroom
            FROM course
            WHERE course.need = "必修"
            AND open_class = (SELECT classname FROM class_list WHERE class_ID =
            %s) """, (class_ID,))
        table = cursor.fetchall()
        insert_haschoose.haschoose(table, username)
        renew_student_credits.haschoose(username)
        return True
    except Exception as e:
        print("Error:", e)
        return None