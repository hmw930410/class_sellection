from flask import Flask, render_template, request, redirect, url_for, session
import login
import show_student_info
import show_student_table
import show_canchoose_table
import add_need_course
import choose_course
import cancel_course

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def loginAction():
    if request.method == 'POST':  
        username = request.form['username']
        password = request.form['password']
        session_data = login.Action(username, password)
        add_need_course.addcourse(username)
        if session_data is not None:
            session['username'] = username
            return redirect('/schedule')
        else:
            error = "帳號或密碼錯誤"
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')


@app.route('/schedule', methods=['GET', 'POST'])
def studentInfo():
    student_id = session.get('username')
    if student_id is not None:
        students = show_student_info.student_info(student_id)
        hastables = show_student_table.student_table(student_id)
        cantables = show_canchoose_table.canchoose(student_id)
        if request.method == 'POST':
            course_id = request.form['input_courseID']
            if 'add' in request.form:
                success, error = choose_course.choosecourse(student_id, course_id)
                if success:
                    return redirect(url_for('studentInfo'))
                else:
                    return render_template('course_schedule.html', error=error,
                                            students=students,
                                            hastables=hastables,
                                            cantables=cantables)

            if 'minus' in request.form:
                success, error = cancel_course.cancelcourse(student_id, course_id)
                if success:
                    return redirect(url_for('studentInfo'))
                else:
                    return render_template('course_schedule.html', error=error,
                                            students=students,
                                            hastables=hastables,
                                            cantables=cantables)

        return render_template('course_schedule.html', students=students,
                               hastables=hastables, cantables=cantables)
    else:
        return redirect(url_for('loginAction'))


if __name__ == '__main__':
    app.run(debug=True)