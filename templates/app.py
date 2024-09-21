from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def connect_db():
    return sqlite3.connect('sichuan_university.db')

def add_student_db(name, year_of_enrollment, major, gender, birth_year, region):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Students (name, year_of_enrollment, major, gender, birth_year, region)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, year_of_enrollment, major, gender, birth_year, region))
    conn.commit()
    conn.close()

def update_student_db(student_id, name, year_of_enrollment, major, gender, birth_year, region):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Students
        SET name = ?, year_of_enrollment = ?, major = ?, gender = ?, birth_year = ?, region = ?
        WHERE student_id = ?
    ''', (name, year_of_enrollment, major, gender, birth_year, region, student_id))
    conn.commit()
    conn.close()

def delete_student_db(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Students WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()

def query_student_db(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Students WHERE student_id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        year_of_enrollment = request.form['year_of_enrollment']
        major = request.form['major']
        gender = request.form['gender']
        birth_year = request.form['birth_year']
        region = request.form['region']
        add_student_db(name, year_of_enrollment, major, gender, birth_year, region)
        flash('Student added successfully!')
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/update_student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        year_of_enrollment = request.form['year_of_enrollment']
        major = request.form['major']
        gender = request.form['gender']
        birth_year = request.form['birth_year']
        region = request.form['region']
        update_student_db(student_id, name, year_of_enrollment, major, gender, birth_year, region)
        flash('Student updated successfully!')
        return redirect(url_for('index'))
    return render_template('update_student.html')

@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        delete_student_db(student_id)
        flash('Student deleted successfully!')
        return redirect(url_for('index'))
    return render_template('delete_student.html')

@app.route('/query_student', methods=['GET', 'POST'])
def query_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student = query_student_db(student_id)
        return render_template('query_student.html', student=student)
    return render_template('query_student.html')

if __name__ == '__main__':
    app.run(debug=True)
