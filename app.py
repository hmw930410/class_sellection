from flask import Flask, render_template
import show_student_info
import show_student_table
import show_canchoose_table
import add_need_course

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def page():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def studentInfo():
    nowstudent = 2
    students = show_student_info.student_info(nowstudent)
    add_need_course.addcourse(nowstudent)
    hastables = show_student_table.student_table(nowstudent)
    cantables = show_canchoose_table.canchoose(nowstudent)
    return render_template(
        'course_schedule.html',
        students=students,
        hastables=hastables,
        cantables=cantables)


if __name__ == '__main__':
    app.run(debug=True)