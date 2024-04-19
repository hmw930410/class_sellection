from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# MySQL 連接設置
db = MySQLdb.connect(host="127.0.0.1",
                     user="test",
                     passwd="123",
                     db="show_sql")

cursor = db.cursor()

# 登入頁面
@app.route('/')
def login_page():
    return render_template('login.html')

# 登入驗證
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # 查詢數據庫
    cursor.execute("SELECT * FROM student WHERE student_ID=%s AND PASSWORD=%s", (username, password))
    user = cursor.fetchone()

    if user:
        # 登入成功，可以添加任何你希望的操作，比如跳轉到其他頁面
        return redirect(url_for('success'))
    else:
        # 登入失敗，可以返回到登入頁面，或者顯示錯誤信息
        return render_template('login.html', error="帳號或密碼錯誤")

# 登入成功頁面
@app.route('/success')
def success():
    return "登入成功！"

if __name__ == '__main__':
    app.run(debug=True)
