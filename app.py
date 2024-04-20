from flask import Flask, render_template
import show_student_info
import show_student_table
import insert_haschoose
import show_canchoose_table
import add_need_course

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def page():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def studentInfo():
    nowstudent = 1
    students = show_student_info.student_info(nowstudent)
    hastables = show_student_table.student_table(nowstudent)
    addneedcourse = add_need_course.addcourse(nowstudent)
    cantables = show_canchoose_table.canchoose(nowstudent)
    return render_template(
        'course_schedule.html',
        students=students,
        hastables=hastables,
        cantables=cantables)


if __name__ == '__main__':
    app.run(debug=True)