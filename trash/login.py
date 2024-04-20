from flask import Flask, render_template, redirect, session
# import trash.login_action as login_action
import show_student_info

    

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')  # 登入頁面
def index():
    return render_template('course_schedule.html')
'''
@app.route('/login', methods=['POST'])  # 登入驗證


def loginAction():
    # username = login_action.userLogin()
    username = None
    if username : 
        return render_template('course_schedule.html', username=username)
    else:
        return render_template('index.html', error="帳號或密碼錯誤")
'''
 

@app.route('/student_info', methods=['POST'])
def studentInfo():  
    # username = session.get('username')
    students = show_student_info.student_info(1)
    return render_template('course_schedule.html', students=students)
'''
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
    app.run(debug=True)