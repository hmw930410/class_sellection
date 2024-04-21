import MySQLdb
import renew_student_credits
import insert_haschoose


def choosecourse(username, courseid):
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        cursor.execute("""SELECT course_name, credits, Max_people,
                                 now_people, department_ID, week,
                                 begin_time, end_time
                          FROM course
                          WHERE course_ID = %s
                       """, (courseid,))
        course_info = cursor.fetchall()
        course_name = course_info[0][0]
        cursor.execute("""SELECT total_credit, department_ID
                          FROM student
                          WHERE student_ID = %s
                       """, (username,))
        student_info = cursor.fetchall()
        cursor.execute("""SELECT COUNT(*)
                  FROM classtable
                  JOIN course ON classtable.course_ID = course.course_ID
                  WHERE classtable.student_ID = %s AND course.course_name = %s
               """, (username, course_name))
        ifchoose = cursor.fetchone()
        table_name = f"student{username}"
        print(course_info[0][6], course_info[0][7])
        for i in range(course_info[0][6], course_info[0][7] + 1):
            cursor.execute(f"""SELECT week, no{i}
                              FROM {table_name}
                              WHERE week = %s AND no{i} = 2
                            """, (course_info[0][5],))
            hascourse = cursor.fetchall()
            if hascourse:
                error = "您此時段已有課程"
                return False, error

        if ifchoose[0] != 0:
            error = "您已選相同名稱之課程"
            return False, error
        elif course_info[0][4] != student_info[0][1]:
            error = "您不能選擇外系課程"
            return False, error
        elif course_info[0][2] == course_info[0][3]:
            error = "該課程人數已滿"
            return False, error
        elif student_info[0][0] + course_info[0][1] > 30:
            error = "您加選後學分超過最高學分限制"
            return False, error
        else:
            cursor.execute("""
            SELECT course.course_ID, course.course_name, course.need,
                   course.class_time, course.teacher, course.classroom
            FROM course
            WHERE course.course_ID = %s
            """, (courseid,))
            table = cursor.fetchall()
            insert_haschoose.haschoose(table, username)
            renew_student_credits.haschoose(username)
            return True, None
    except Exception as e:
        print("Error:", e)
        return False, "An error occurred while choosing the course."
