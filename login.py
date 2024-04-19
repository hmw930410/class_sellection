from flask import Flask, render_template, request, redirect
import MySQLdb

login = Flask(__name__)

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
        return render_template('course_schedule.html')
    else:
        return render_template('index.html', error="帳號或密碼錯誤")


@login.route('/success', methods=['POST'])
def success():
    go_login = request.form.get("inside")
    if go_login:
        return redirect('/course_schedule.html')


if __name__ == '__main__':
    login.run(debug=True)