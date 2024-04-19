from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# MySQL 連線設置
db = MySQLdb.connect(host="127.0.0.1",
                     user="test",
                     passwd="123",
                     db="show_sql")

cursor = db.cursor()


@app.route('/')  # 登入頁面
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])  # 登入驗證
def login():
    username = request.form['username']
    password = request.form['password']

    # 查詢數據庫
    cursor.execute("""
                   SELECT *
                   FROM student
                   WHERE student_ID = "%s"
                   AND PASSWORD = "%s"
                   """, (username, password))
    user = cursor.fetchone()

    if user:
        return redirect(url_for('course_schedul.html'))
    else:
        return render_template('login.html', error="帳號或密碼錯誤")


@app.route('/success')
def success():
    return "登入成功!"


if __name__ == '__main__':
    app.run(debug=True)