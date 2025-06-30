# ================= app.py =================

from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
DB_PATH = 'db/student_db.sqlite3'

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

        # Image handling
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = student['profile_pic']  # Keep existing image

        conn.execute('''UPDATE students SET
            name=?, email=?, phone=?, hallticket=?, dob=?, address=?, profile_pic=?, password=?,
            tenth_htno=?, tenth_result=?, twelfth_htno=?, twelfth_result=?, year=?, branch=?, doj=?,
            sem_1_1=?, sem_1_2=?, sem_2_1=?, sem_2_2=?, sem_3_1=?, sem_3_2=?, sem_4_1=?, sem_4_2=?,
            s11_1=?, s11_2=?, s11_3=?, s11_4=?, s11_5=?, s11_6=?, s11_7=?, s11_8=?, s11_9=?,
            s12_1=?, s12_2=?, s12_3=?, s12_4=?, s12_5=?, s12_6=?, s12_7=?, s12_8=?,
            s21_1=?, s21_2=?, s21_3=?, s21_4=?, s21_5=?, s21_6=?, s21_7=?, s21_8=?, s21_9=?,
            s22_1=?, s22_2=?, s22_3=?, s22_4=?, s22_5=?, s22_6=?, s22_7=?, s22_8=?, s22_9=?,
            s31_1=?, s31_2=?, s31_3=?, s31_4=?, s31_5=?, s31_6=?, s31_7=?, s31_8=?, s31_9=?, s31_10=?,
            s32_1=?, s32_2=?, s32_3=?, s32_4=?, s32_5=?, s32_6=?, s32_7=?, s32_8=?, s32_9=?, s32_10=?,
            s41_1=?, s41_2=?, s41_3=?, s41_4=?, s41_5=?, s41_6=?, s41_7=?, s41_8=?,
            s42_1=?
            WHERE id=?
        ''', (
            form.get('name',''), form.get('email',''), form.get('phone',''), form.get('hallticket',''), form.get('dob',''), form.get('address',''),
            filename, form.get('hallticket',''),  # profile_pic and password both updated
            form.get('tenth_htno',''), form.get('tenth_result',''), form.get('twelfth_htno',''), form.get('twelfth_result',''),
            form.get('year',''), form.get('branch',''), form.get('doj',''),

            form.get('sem_1_1',''), form.get('sem_1_2',''), form.get('sem_2_1',''), form.get('sem_2_2',''),
            form.get('sem_3_1',''), form.get('sem_3_2',''), form.get('sem_4_1',''), form.get('sem_4_2',''),

            form.get('s11_1',''), form.get('s11_2',''), form.get('s11_3',''), form.get('s11_4',''), form.get('s11_5',''),
            form.get('s11_6',''), form.get('s11_7',''), form.get('s11_8',''), form.get('s11_9',''),

            form.get('s12_1',''), form.get('s12_2',''), form.get('s12_3',''), form.get('s12_4',''),
            form.get('s12_5',''), form.get('s12_6',''), form.get('s12_7',''), form.get('s12_8',''),

            form.get('s21_1',''), form.get('s21_2',''), form.get('s21_3',''), form.get('s21_4',''),
            form.get('s21_5',''), form.get('s21_6',''), form.get('s21_7',''), form.get('s21_8',''), form.get('s21_9',''),

            form.get('s22_1',''), form.get('s22_2',''), form.get('s22_3',''), form.get('s22_4',''),
            form.get('s22_5',''), form.get('s22_6',''), form.get('s22_7',''), form.get('s22_8',''), form.get('s22_9',''),

            form.get('s31_1',''), form.get('s31_2',''), form.get('s31_3',''), form.get('s31_4',''), form.get('s31_5',''),
            form.get('s31_6',''), form.get('s31_7',''), form.get('s31_8',''), form.get('s31_9',''), form.get('s31_10',''),

            form.get('s32_1',''), form.get('s32_2',''), form.get('s32_3',''), form.get('s32_4',''), form.get('s32_5',''),
            form.get('s32_6',''), form.get('s32_7',''), form.get('s32_8',''), form.get('s32_9',''), form.get('s32_10',''),

            form.get('s41_1',''), form.get('s41_2',''), form.get('s41_3',''), form.get('s41_4',''),
            form.get('s41_5',''), form.get('s41_6',''), form.get('s41_7',''), form.get('s41_8',''),

            form.get('s42_1',''), id
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

        # Handle image upload
        image = request.files['profile_pic']
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = 'default.png'  # Or leave blank if no image provided

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