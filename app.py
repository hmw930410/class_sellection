from flask import Flask, render_template
import show_student_info
import show_student_table
app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def page():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def studentInfo():
    nowstudent = 1
    students = show_student_info.student_info(nowstudent)
    tables = show_student_table.student_table(nowstudent)
    return render_template(
        'course_schedule.html',
        students=students,
        tables=tables)


if __name__ == '__main__':
    app.run(debug=True)