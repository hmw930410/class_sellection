import MySQLdb
import renew_student_credits
import delete_choose


def cancelcourse(username, courseid):

    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        cursor.execute("""SELECT course_name, need, credits, open_class,
                                 week, begin_time, end_time
                          FROM course
                          WHEHRE course_ID = %s
                       """, (courseid,))
        course_info = cursor.fetchall()
        cursor.execute("""SELECT student.total_credit, class_list.classname
                          FROM student
                          JOIN class_list ON student.class_ID = class_list.class_ID
                          WHERE student.student_ID = %s
                       """, (username,))
        student_info = cursor.fetchall()
        if student_info[0][0] - course_info[0][3] < 9:
            error = "您加選後學分超過最高學分限制"
            return False, error
    except Exception as e:
        print("Error:", e)
        return False, "Error."