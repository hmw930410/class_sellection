from flask import Flask, render_template, redirect, session
import login_action

login = Flask(__name__)
login.secret_key = 'key'


@login.route('/')  # 登入頁面
def login_page():
    return render_template('index.html')


@login.route('/login', methods=['POST'])  # 登入驗證
def login_action():
    username = login_action.userLogin()
    if username:
        session['username'] = username
        return render_template('course_schedule.html', username=username)
    else:
        return render_template('index.html', error="帳號或密碼錯誤")

'''

@login.route('/course_schedule', methods=['POST'])
def student_info():
    username = session.get('username')
    if username:
        cursor.execute("""
            SELECT student.student_ID, student.student_name, class_list.classname, student.total_credit
            FROM student
            JOIN class_list ON student.class_ID = class_list.class_ID
            WHERE student.student_ID = %s
        """, (username,))
        students = cursor.fetchall()
        return render_template('course_schedule.html', students=students)
    else:
        return redirect('/')
    
def schedule():
    username = session.get('username')
    
    if username:
        cursor.execute("""
            SELECT coures.course_ID, course.course_name, course.class_time, course.teacher, course.classroom
            FROM course 
            INNER JOIN classtable ON course.course_ID = classtable.course_ID
            WHERE classtable.student_ID = %s
        """, (username,))
        courses = cursor.fetchall()  # 獲取查詢結果
        return render_template('course_schedule.html', courses=courses)  # 關閉資料庫連接
    else:
        return redirect('/')
'''
if __name__ == '__main__':
    login.run(debug=True)