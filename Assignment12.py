""""
part 1 - Database Setup and Initialization
-----------------------------------------
Need 3 entities: 1) Students, 2), Quizzes, Student's Results on Quizzes

1) Students table requires:
    a) First name (e.g. 'John')
    b) last name (e.g. 'Smith')
    c) unique id
2) Quizzes table requires:
    a) unique id
    b) subject name (e.g. Python Basics)
    c) number of questions (e.g. '5')
    d) quiz date (e.g 'February 5th, 2015')
3) Student result table links quiz to student (one-to-one) with score (0-100)

Part 2 - Teacher Login

Create login route rendering simple login form where username and password could be requested
should submit to '/login' route,
If logged in, should route to "/dashboard"
2 username should be 'admin
 and password 'password'
"""

from flask import Flask, render_template, url_for, redirect
import sqlite3

con = sqlite3.connect(':memory:')

#not generationg student
with con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY AUTOINCREMENT,
     first_name TEXT, last_name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes(quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
     subject TEXT, number_of_qs INT, quiz_date TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS student_quizzes(sq_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INT NOT NULL, quiz_id INT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS results(result_id INTEGER PRIMARY KEY AUTOINCREMENT,
     student_result INT NOT NULL, student_score INT NOT NULL,
     FOREIGN KEY (student_result) REFERENCES student_quizzes(sq_id))''')

    cursor.execute("""INSERT OR IGNORE INTO students(student_id, first_name, last_name)
                   VALUES(?,?, ?)""", (1, 'John', 'Oliver'))
    cursor.execute("""INSERT OR IGNORE INTO students(first_name, last_name)
                   VALUES(?,?)""", ('John', 'Smith'))
    cursor.execute("""INSERT OR IGNORE INTO students(first_name, last_name)
                    VALUES(?,?)""", ('Jane', 'Doe'))

    cursor.execute("""INSERT OR IGNORE INTO quizzes(subject, number_of_qs, quiz_date)
                VALUES(?,?,?)""", ('Basic Python', 25, '10/22/2019'))
    cursor.execute("""INSERT OR IGNORE INTO quizzes(subject, number_of_qs, quiz_date)
                VALUES (?,?,?)""", ('Intro to Calculus', 50, '8/11/2019'))
    cursor.execute("""INSERT OR IGNORE INTO quizzes(subject, number_of_qs, quiz_date)
                VALUES (?,?,?)""", ('Algebra', 35, '1/1/2019'))

    cursor.execute("""INSERT OR IGNORE INTO student_quizzes(student_id, quiz_id)
                    VALUES(?,?)""", ('1','1'))
    cursor.execute("""INSERT OR IGNORE INTO student_quizzes(student_id, quiz_id)
                    VALUES(?,?)""", ('1','2'))
    cursor.execute("""INSERT OR IGNORE INTO student_quizzes(student_id, quiz_id)
                    VALUES(?,?)""", ('2','3'))

    cursor.execute('''INSERT OR IGNORE INTO results(student_result, student_score)
      VALUES (?,?)''', ('1', '75'))
    cursor.execute('''INSERT OR IGNORE INTO results(student_result, student_score)
     VALUES (?,?)''', ('2', '80'))
    cursor.execute('''INSERT OR IGNORE INTO results(student_result, student_score)
    VALUES (?,?)''', ('3', '60'))

    cursor.execute('''SELECT * FROM students''')

    cursor.execute('''SELECT * FROM quizzes ''')

    cursor.execute("""SELECT students.first_name, students.last_name, results.student_score,
     quizzes.subject FROM results
     JOIN students
     ON students.student_id == results.student_result""
     JOIN Equizzes
     ON student_quizzes.quiz_id == quizzes.quiz_id""")

#    (SELECT subject FROM quizzes.quiz_id == student_quizzes.quiz_id)

    rows = cursor.fetchall()

con.commit()

for row in rows:
    print (row)

"""
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def main_page():
    return 'Please enter Your Login and Password!'

if __name__ == '__main__':
    app.run(debug=True)
"""
@app.route('/dashboard/<name>')
def home(name):
    return 'Welcome %s'% name

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            #session['logged_in'] = True
            return 'Hello'
    #else:
    #    flash('Username and/or password is incorrect. Please try again.')

@app.route('/dashboard')
def dashboard():
    pass

if __name__ == '__main__':
    app.run(debug=True)
    
