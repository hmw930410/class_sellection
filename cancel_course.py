from flask import render_template
import show_student_info
import MySQLdb
import renew_student_credits
import insert_haschoose

def cancelcourse(username, courseid):
    
    try:
        db = MySQLdb.connect(host="127.0.0.1",
                             user="test",
                             passwd="123",
                             db="show_sql")
        cursor = db.cursor()
        
        