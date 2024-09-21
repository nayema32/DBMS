from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sichuan_university.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        year_of_enrollment = request.form['year_of_enrollment']
        major = request.form['major']
        gender = request.form['gender']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Students (student_id, name, year_of_enrollment, major, gender, email, phone_number, address)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, name, year_of_enrollment, major, gender, email, phone_number, address))
            conn.commit()
        except sqlite3.IntegrityError as e:
            conn.rollback()
            print(f"Error: {e}")
        finally:
            conn.close()

        return redirect(url_for('index'))

    return render_template('add_student.html')

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM Students').fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/update_student>', methods=['GET', 'POST'])
def update_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form.get('name')
        year_of_enrollment = request.form.get('year_of_enrollment')
        major = request.form.get('major')
        gender = request.form.get('gender')
        birth_year = request.form.get('birth_year')
        region = request.form.get('region')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')

        try:
            cursor.execute('''
                UPDATE Students 
                SET name = ?, year_of_enrollment = ?, major = ?, gender = ?, birth_year = ?, region = ?, email = ?, phone_number = ?
                WHERE student_id = ?
            ''', (name, year_of_enrollment, major, gender, birth_year, region, email, phone_number, student_id))
            conn.commit()
            return redirect(url_for('students'))
        except sqlite3.IntegrityError as e:
            conn.rollback()
            print(f"Error updating student: {e}")
        finally:
            conn.close()

    # Fetch current student data for pre-filling the form
    cursor.execute('SELECT * FROM Students WHERE student_id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()

    if student:
        return render_template('update_student.html', student=student)
    else:
        return 'Student not found', 404


if __name__ == "__main__":
    app.run(debug=True)
