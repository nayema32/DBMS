from flask import Flask, render_template, request, redirect, url_for, flash
from db_operations import connect_db, add_student_db, update_student_db, delete_student_db, query_student_db

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Add Student
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

# Update Student
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

# Delete Student
@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        delete_student_db(student_id)
        flash('Student deleted successfully!')
        return redirect(url_for('index'))
    return render_template('delete_student.html')

# Query Student
@app.route('/query_student', methods=['GET', 'POST'])
def query_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student = query_student_db(student_id)
        return render_template('query_student.html', student=student)
    return render_template('query_student.html')

if __name__ == '__main__':
    app.run(debug=True)
