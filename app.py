# ================= app.py =================

from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_PATH = 'db/student_db.sqlite3'

# Folder to store profile pictures
app.config['UPLOAD_FOLDER'] = 'static/images'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect('/admin_dashboard')
        else:
            return 'Invalid credentials'
    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('admin_dashboard.html', students=students)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        form = request.form
        image = request.files.get('profile_pic')
        filename = student['profile_pic'] or 'default.png'

        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn.execute('''
            UPDATE students SET
                name=?, email=?, phone=?, hallticket=?, dob=?, address=?,
                profile_pic=?, password=?, tenth_htno=?, tenth_result=?,
                twelfth_htno=?, twelfth_result=?, year=?, branch=?, doj=?
            WHERE id=?
        ''', (
            form.get('name',''), form.get('email',''), form.get('phone',''), form.get('hallticket',''),
            form.get('dob',''), form.get('address',''), filename, form.get('hallticket',''),
            form.get('tenth_htno',''), form.get('tenth_result',''),
            form.get('twelfth_htno',''), form.get('twelfth_result',''),
            form.get('year',''), form.get('branch',''), form.get('doj',''), id
        ))
        conn.commit()
        conn.close()
        return redirect('/admin_dashboard')

    return render_template('edit_student.html', student=student)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    if request.method == 'POST':
        form = request.form
        hallticket = form.get('hallticket', '')
        image = request.files.get('profile_pic')
        
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = 'default.png'

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO students (
                name, email, phone, hallticket, dob, address, profile_pic,
                tenth_htno, tenth_result, twelfth_htno, twelfth_result,
                year, branch, doj, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            form.get('name', ''),
            form.get('email', ''),
            form.get('phone', ''),
            hallticket,
            form.get('dob', ''),
            form.get('address', ''),
            filename,
            form.get('tenth_htno', ''),
            form.get('tenth_result', ''),
            form.get('twelfth_htno', ''),
            form.get('twelfth_result', ''),
            form.get('year', ''),
            form.get('branch', ''),
            form.get('doj', ''),
            hallticket
        ))
        conn.commit()
        conn.close()
        return redirect('/admin_dashboard')

    return render_template('add_student.html')



@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE email = ? AND password = ?', (email, password)).fetchone()
        conn.close()
        if student:
            session['student_id'] = student['id']
            return redirect('/student_dashboard')
        else:
            return 'Invalid credentials'
    return render_template('student_login.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'student_id' not in session:
        return redirect('/student_login')
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (session['student_id'],)).fetchone()
    conn.close()
    return render_template('student_dashboard.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/admin_dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)