from flask import Flask, render_template, request, redirect, url_for, session
import login
import show_student_info
import show_student_table
import show_canchoose_table
import add_need_course

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def loginAction():
    if request.method == 'POST':  # 檢查用戶的請求是否是 POST 方法
        username = request.form['username']
        password = request.form['password']
        session_data = login.Action(username, password)
        if session_data is not None:
            session['username'] = username
            return redirect('/schedule')
        else:
            error = "Incorrect username/password"
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')


@app.route('/schedule')
def studentInfo():
    student_id = session.get('username')
    if student_id is not None:
        print(student_id)
        students = show_student_info.student_info(student_id)
        add_need_course.addcourse(student_id)
        hastables = show_student_table.student_table(student_id)
        cantables = show_canchoose_table.canchoose(student_id)
        return render_template(
            'course_schedule.html',
            students=students,
            hastables=hastables,
            cantables=cantables)
    else:
        return redirect(url_for('loginAction'))


if __name__ == '__main__':
    app.run(debug=True)