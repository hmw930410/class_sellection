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
                
                cursor.execute("""SELECT week, begin_time, end_time
                                  From course
                                  WHERE course_ID = %s
                               """, (course_ID,))
                course_info = cursor.fetchone()
                for i in range(course_info[1], course_info[2] + 1):
                    table_name = f"student{username}"  # 使用 f-strings 生成表格名稱
                    cursor.execute(f"""UPDATE {table_name} SET no{i} = 2
                                       WHERE week = {course_info[0]}""")
        db.commit()

        return table
    except Exception as e:
        print("error:", e)
        db.rollback()
        return None
    finally:
        cursor.close()
        db.close()