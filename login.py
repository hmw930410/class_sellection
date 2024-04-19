from flask import Flask, render_template, request, redirect, session
import MySQLdb

login = Flask(__name__)


login.secret_key = 'key'
# MySQL 連線設置
db = MySQLdb.connect(host="127.0.0.1",
                     user="test",
                     passwd="123",
                     db="show_sql")

cursor = db.cursor()


@login.route('/')  # 登入頁面
def login_page():
    return render_template('index.html')


@login.route('/login', methods=['POST'])  # 登入驗證
def login_action():
    username = request.form['username']
    password = request.form['password']

    # 查詢數據庫
    cursor.execute("""
                   SELECT *
                   FROM student
                   WHERE student_ID = %s
                   AND PASSWORD = %s
                   """, (username, password))
    user = cursor.fetchone()

    if user:
        session['username'] = username
        return render_template('course_schedule.html')
    else:
        return render_template('index.html', error="帳號或密碼錯誤")


@login.route('/course_schedule', methods=['GET'])
def course_schedule():
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

if __name__ == '__main__':
    login.run(debug=True)